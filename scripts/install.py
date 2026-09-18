#!/usr/bin/env python3
"""Copy standalone skills into a selected host directory, without network calls."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile


def frontmatter(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
    if not match:
        raise ValueError("Missing or unclosed skill frontmatter")
    return match[1]


def skill_directories(repo):
    result = {}
    for entry in sorted((Path(repo) / "skills").iterdir()):
        if not entry.is_dir() or not (entry / "SKILL.md").is_file():
            continue
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry.name):
            raise ValueError(f"Invalid skill directory: {entry.name}")
        if entry.is_symlink() or any(p.is_symlink() for p in entry.rglob("*")):
            raise ValueError(f"Symlinks are not supported: {entry.name}")
        content = (entry / "SKILL.md").read_text(encoding="utf-8")
        metadata = frontmatter(content)
        matches = re.findall(r"^name:[ \t]*([a-z0-9-]+)[ \t]*$", metadata, re.M)
        if matches != [entry.name]:
            raise ValueError(f"Skill name does not match directory: {entry.name}")
        result[entry.name] = entry
    return result


def hashes(directory):
    return {
        str(p.relative_to(directory)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(directory.rglob("*")) if p.is_file()
    }


def install(repo, destination, names=None, dry_run=False):
    available = skill_directories(repo)
    selected = list(dict.fromkeys(names or available))
    unknown = sorted(set(selected) - set(available))
    if unknown:
        raise ValueError(f"Unknown skill(s): {', '.join(unknown)}")
    if not selected:
        raise ValueError("No skills found")
    destination = Path(destination).expanduser().absolute()
    if destination.is_symlink():
        raise ValueError("Destination must not be a symlink")
    if destination.exists() and not destination.is_dir():
        raise ValueError("Destination is not a directory")
    # Preflight every target before copying any; never replace a user's skill.
    for name in selected:
        target = destination / name
        if target.exists() or target.is_symlink():
            raise FileExistsError(f"Already exists: {target}. Back up and compare before updating.")
    report = {"dry_run": dry_run, "destination": str(destination), "skills": []}
    for name in selected:
        source = available[name]
        report["skills"].append({"name": name, "files": len(hashes(source))})
    if dry_run:
        return report
    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".qbs-stage-", dir=destination) as stage:
        for name in selected:
            source = available[name]
            staged = Path(stage) / name
            shutil.copytree(source, staged)
            if hashes(source) != hashes(staged):
                raise OSError(f"Copy verification failed: {name}")
        completed = []
        for name in selected:
            target = destination / name
            # Reserve exclusively; rename replaces only this empty directory.
            # A concurrent writer making it nonempty causes rename to fail.
            target.mkdir()
            try:
                (Path(stage) / name).rename(target)
            except OSError as exc:
                try:
                    target.rmdir()  # Empty reservation only; preserve foreign files.
                except OSError:
                    pass
                raise OSError(f"Install stopped at {name}; preserved completed packages {completed}: {exc}") from exc
            completed.append(name)
            if hashes(available[name]) != hashes(target):
                raise OSError(f"Installed readback changed: {name}; files preserved for inspection")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, required=True,
                        help="Host skill directory, for example ~/.codex/skills")
    parser.add_argument("--skill", action="append", help="Skill name; repeat to select. Default: all")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        result = install(Path(__file__).resolve().parents[1], args.dest, args.skill, args.dry_run)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Install stopped: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

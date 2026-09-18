#!/usr/bin/env python3
"""Offline packaging checks. This does not evaluate model decisions."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse, unquote

from install import frontmatter, skill_directories


def local_links(path):
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        target = target.split("#", 1)[0].strip("<>")
        if not target or urlparse(target).scheme:
            continue
        yield unquote(target)


def validate(repo):
    repo = Path(repo).resolve()
    errors = []
    skills = skill_directories(repo)
    library = json.loads((repo / "skills/qbs/references/library.json").read_text())
    if library.get("schema_version") != 1:
        errors.append("Unsupported library schema")
    seen_ids, seen_skills = set(), set()
    required = {"id", "title", "author", "isbn", "skill", "skill_path", "book_path",
                "scope", "reading_scope", "source_url", "cover_url", "book_url", "status"}
    for book in library.get("books", []):
        missing = required - book.keys()
        if missing:
            errors.append(f"Missing book fields: {sorted(missing)}")
            continue
        if book["id"] in seen_ids or book["skill"] in seen_skills:
            errors.append(f"Duplicate book or skill: {book['id']}")
        seen_ids.add(book["id"])
        seen_skills.add(book["skill"])
        if book["skill"] not in skills:
            errors.append(f"Missing registered skill: {book['skill']}")
        if book["status"] not in {"draft", "simulated", "field-tested"}:
            errors.append(f"Invalid evidence status: {book['id']}")
        if book["skill_path"] != f"skills/{book['skill']}":
            errors.append(f"Mismatched skill path: {book['id']}")
        book_page = (repo / book["book_path"]).resolve()
        if not book_page.is_relative_to(repo) or not book_page.is_file():
            errors.append(f"Missing or escaping book page: {book['id']}")
            continue
        page_text = book_page.read_text(encoding="utf-8")
        if book["cover_url"] not in page_text or not (
            re.search(r"!\[[^\]]*\]\(" + re.escape(book["cover_url"]) + r"\)", page_text)
            or re.search(r'<img\b[^>]*src=[\"\x27]' + re.escape(book["cover_url"]), page_text)
        ):
            errors.append(f"Book page must display registered cover: {book['id']}")
        for key in ("source_url", "cover_url", "book_url"):
            if urlparse(book[key]).scheme != "https":
                errors.append(f"Non-HTTPS {key}: {book['id']}")
    for name, skill in skills.items():
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        if not re.search(r"^description:[ \t]*\S", frontmatter(text), re.M):
            errors.append(f"Missing description: {name}")
        ui = skill / "agents/openai.yaml"
        if not ui.is_file() or f"${name}" not in ui.read_text(encoding="utf-8"):
            errors.append(f"Missing invocation metadata: {name}")
        for md in skill.rglob("*.md"):
            for target in local_links(md):
                resolved = (md.parent / target).resolve()
                if not resolved.is_file():
                    errors.append(f"Broken skill reference: {md.relative_to(repo)} -> {target}")
                elif not resolved.is_relative_to(skill):
                    errors.append(f"Runtime reference outside standalone skill: {name} -> {target}")
    documentation = (list(repo.glob("README*.md"))
                     + list((repo / "books").glob("*.md"))
                     + list((repo / "docs").glob("*.md")))
    for md in documentation:
        if md.is_file():
            for target in local_links(md):
                if not (md.parent / target).resolve().exists():
                    errors.append(f"Broken documentation link: {md.relative_to(repo)} -> {target}")
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    try:
        failures = validate(root)
    except (OSError, ValueError, KeyError) as exc:
        failures = [str(exc)]
    if failures:
        print("\n".join(failures), file=sys.stderr)
        sys.exit(1)
    print("PASS: skill packages, standalone references, book catalog, covers and documentation links")

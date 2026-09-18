import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("qbs_install", REPO / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dest = Path(self.temp.name) / "skills"

    def test_dry_run_makes_no_directory(self):
        report = installer.install(REPO, self.dest, dry_run=True)
        self.assertTrue(report["dry_run"])
        self.assertFalse(self.dest.exists())
        self.assertEqual({s["name"] for s in report["skills"]}, {"qbs", "make-time", "shape-up", "the-debugging-book"})

    def test_all_packages_read_back_identically(self):
        installer.install(REPO, self.dest)
        for name, source in installer.skill_directories(REPO).items():
            self.assertEqual(installer.hashes(source), installer.hashes(self.dest / name))

    def test_child_can_install_alone(self):
        for name in ("make-time", "shape-up", "the-debugging-book"):
            with self.subTest(skill=name):
                dest = self.dest / name
                installer.install(REPO, dest, [name])
                self.assertEqual({p.name for p in dest.iterdir()}, {name})
                self.assertEqual(installer.hashes(REPO / "skills" / name),
                                 installer.hashes(dest / name))
                self.assertTrue((dest / name / "references/source-notes.md").is_file())

    def test_parent_can_install_alone(self):
        installer.install(REPO, self.dest, ["qbs"])
        self.assertFalse((self.dest / "make-time").exists())
        self.assertTrue((self.dest / "qbs/references/library.json").is_file())

    def test_existing_target_stops_all_copies(self):
        existing = self.dest / "qbs"
        existing.mkdir(parents=True)
        sentinel = existing / "local-user-rule.md"
        sentinel.write_text("keep this edit")
        with self.assertRaises(FileExistsError):
            installer.install(REPO, self.dest)
        self.assertEqual(sentinel.read_text(), "keep this edit")
        self.assertFalse((self.dest / "make-time").exists())

    def test_unknown_or_traversal_name_rejected(self):
        for name in ("missing", "../escape", "/tmp/escape"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                installer.install(REPO, self.dest, [name])
        self.assertFalse(self.dest.exists())

    def test_symlink_source_rejected(self):
        repo = Path(self.temp.name) / "repo"
        skill = repo / "skills/demo"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: demo\ndescription: test\n---\n")
        (skill / "outside").symlink_to(REPO / "LICENSE")
        with self.assertRaises(ValueError):
            installer.install(repo, self.dest)
        self.assertFalse(self.dest.exists())

    def test_existing_symlink_target_preserved(self):
        self.dest.mkdir()
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (outside / "keep").write_text("untouched")
        (self.dest / "qbs").symlink_to(outside)
        with self.assertRaises(FileExistsError):
            installer.install(REPO, self.dest)
        self.assertEqual((outside / "keep").read_text(), "untouched")

    def test_staging_failure_leaves_no_installed_packages(self):
        self.dest.mkdir()
        (self.dest / "unrelated").write_text("keep")
        real_copy = installer.shutil.copytree
        def fail_final_copy(src, dst, *args, **kwargs):
            if Path(src) == REPO / "skills/qbs":
                raise OSError("simulated disk failure")
            return real_copy(src, dst, *args, **kwargs)
        with patch.object(installer.shutil, "copytree", side_effect=fail_final_copy):
            with self.assertRaises(OSError):
                installer.install(REPO, self.dest)
        self.assertEqual(list(self.dest.iterdir()), [self.dest / "unrelated"])
        self.assertEqual((self.dest / "unrelated").read_text(), "keep")

    def test_concurrent_user_file_is_preserved(self):
        real_rename = Path.rename
        def concurrent_write(staged, target):
            if Path(target) == self.dest / "qbs":
                (Path(target) / "user-notes.md").write_text("concurrent edit")
            return real_rename(staged, target)
        with patch.object(Path, "rename", new=concurrent_write):
            with self.assertRaises(OSError):
                installer.install(REPO, self.dest)
        self.assertEqual((self.dest / "qbs/user-notes.md").read_text(), "concurrent edit")
        self.assertEqual(installer.hashes(REPO / "skills/make-time"),
                         installer.hashes(self.dest / "make-time"))

    def test_publish_failure_removes_only_empty_reservation(self):
        real_rename = Path.rename
        def fail_rename(staged, target):
            if Path(target) == self.dest / "qbs":
                raise OSError("simulated failure")
            return real_rename(staged, target)
        with patch.object(Path, "rename", new=fail_rename):
            with self.assertRaises(OSError):
                installer.install(REPO, self.dest)
        self.assertFalse((self.dest / "qbs").exists())
        self.assertTrue((self.dest / "make-time/SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()

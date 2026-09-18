import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
from validate import validate


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        for name in ("skills", "books"):
            shutil.copytree(REPO / name, self.repo / name)

    def test_current_packages_are_valid(self):
        self.assertEqual(validate(self.repo), [])

    def test_missing_source_reference_is_rejected(self):
        (self.repo / "skills/high-output-management/references/source-notes.md").unlink()
        self.assertTrue(any("Broken skill reference" in s for s in validate(self.repo)))

    def test_unclosed_frontmatter_is_rejected(self):
        entry = self.repo / "skills/qbs/SKILL.md"
        entry.write_text(entry.read_text().replace("\n---\n", "\n", 1))
        with self.assertRaises(ValueError):
            validate(self.repo)

    def test_body_description_does_not_count_as_metadata(self):
        entry = self.repo / "skills/qbs/SKILL.md"
        text = entry.read_text()
        metadata, body = text.split("\n---\n", 1)
        metadata = "\n".join(line for line in metadata.splitlines() if not line.startswith("description:"))
        entry.write_text(metadata + "\n---\n" + body + "\ndescription: only in body\n")
        self.assertTrue(any("Missing description" in s for s in validate(self.repo)))

    def test_parent_dependency_in_child_is_rejected(self):
        entry = self.repo / "skills/high-output-management/SKILL.md"
        with entry.open("a") as f:
            f.write("\n[required parent](../qbs/SKILL.md)\n")
        self.assertTrue(any("outside standalone" in s for s in validate(self.repo)))

    def test_cover_removal_is_rejected(self):
        page = self.repo / "books/high-output-management.md"
        page.write_text("# A book page with no cover")
        self.assertTrue(any("display registered cover" in s for s in validate(self.repo)))

    def test_catalog_path_escape_is_rejected(self):
        catalog = self.repo / "skills/qbs/references/library.json"
        data = json.loads(catalog.read_text())
        data["books"][0]["book_path"] = "../outside.md"
        catalog.write_text(json.dumps(data))
        self.assertTrue(any("escaping book page" in s for s in validate(self.repo)))

    def test_duplicate_catalog_entry_is_rejected(self):
        catalog = self.repo / "skills/qbs/references/library.json"
        data = json.loads(catalog.read_text())
        data["books"].append(data["books"][0].copy())
        catalog.write_text(json.dumps(data))
        self.assertTrue(any("Duplicate book" in s for s in validate(self.repo)))

    def test_missing_translation_link_is_rejected(self):
        (self.repo / "README.en.md").write_text("[日本語](README.ja.md)\n", encoding="utf-8")
        self.assertIn("Broken documentation link: README.en.md -> README.ja.md", validate(self.repo))

    def test_language_switches_resolve_between_readmes(self):
        (self.repo / "README.md").write_text("[English](README.en.md)\n")
        (self.repo / "README.en.md").write_text("[日本語](README.ja.md)\n", encoding="utf-8")
        (self.repo / "README.ja.md").write_text("[中文](README.md)\n", encoding="utf-8")
        self.assertEqual(validate(self.repo), [])

    def test_missing_documentation_link_is_rejected(self):
        docs = self.repo / "docs"
        docs.mkdir()
        (docs / "install.md").write_text("[instructions](missing.md)\n")
        self.assertIn("Broken documentation link: docs/install.md -> missing.md", validate(self.repo))


if __name__ == "__main__":
    unittest.main()

"""Synthetic tests for the offline checker, not the AI skill."""

from pathlib import Path
import tempfile
import unittest

from check_repository import anchors, check, links


class RepositoryChecks(unittest.TestCase):
    def run_case(self, files):
        with tempfile.TemporaryDirectory(prefix="book-skill-check-") as folder:
            root = Path(folder)
            for name, text in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
            return check(root, files)

    def test_nested_markdown_image_and_html_links(self):
        self.assertEqual(links('[![Picture](figure.svg)](SKILL.md) <a href="LICENSE">Licence</a>'),
                         ["figure.svg", "SKILL.md", "LICENSE"])

    def test_valid_links_and_encoded_filename(self):
        errors, counts = self.run_case({
            "README.md": '[Page](pages/One%20Page.md#hello) [Folder](pages/) <img src="figure.svg">',
            "pages/One Page.md": '# Hello\n[Back](../README.md)',
            "figure.svg": '<svg xmlns="http://www.w3.org/2000/svg"/>',
        })
        self.assertEqual(errors, [])
        self.assertEqual(counts, (2, 4, 1))

    def test_missing_file(self):
        errors, _ = self.run_case({"README.md": "[Missing](missing.md)"})
        self.assertIn("missing relative link", errors[0])

    def test_heading_anchor_and_duplicate(self):
        self.assertEqual(anchors("# Hello\n## Hello\n"), {"hello", "hello-1"})
        errors, _ = self.run_case({"README.md": "# Hello\n[Missing](#absent)"})
        self.assertIn("missing heading anchor", errors[0])

    def test_external_links_not_requested(self):
        errors, counts = self.run_case({"README.md": "[External](https://example.invalid/)"})
        self.assertEqual(errors, [])
        self.assertEqual(counts, (1, 0, 0))

    def test_escape_rejected(self):
        errors, _ = self.run_case({"README.md": "[Outside](../outside.md)"})
        self.assertIn("escapes repository", errors[0])

    def test_punctuation(self):
        for character in "\u2013\u2014\u2018\u2019\u201c\u201d":
            with self.subTest(character=ord(character)):
                errors, _ = self.run_case({"README.md": character})
                self.assertIn("non-ASCII dash or smart quote", errors[0])

    def test_malformed_svg(self):
        errors, _ = self.run_case({"figure.svg": "<svg>"})
        self.assertIn("invalid SVG XML", errors[0])


if __name__ == "__main__":
    unittest.main()

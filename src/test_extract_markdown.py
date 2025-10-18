import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_images_captures_images(self):
        text = "This has an ![alt text](https://example.com) image"
        matches = extract_markdown_images(text)
        self.assertEqual(
            matches,
            [("alt text", "https://example.com")]
        )

    def test_images_does_not_capture_link(self):
        text = "This has a [click me](https://example.com) link"
        matches = extract_markdown_images(text)
        self.assertFalse(matches)

    def test_links_captures_links(self):
        text = "This has a [click me](https://example.com) link"
        matches = extract_markdown_links(text)
        self.assertEqual(
            matches,
            [("click me", "https://example.com")]
        )

    def test_links_does_not_capture_images(self):
        text = """This has a [click me](https://example.com) link
                  and an ![alt text](https://example.com) image"""
        matches = extract_markdown_links(text)
        self.assertEqual(
            matches,
            [("click me", "https://example.com")]
        )


if __name__ == "__main__":
    _ = unittest.main()

import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks_multiple_blocks(self):
        markdown = """
This is a **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "This is a **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_single_block(self):
        markdown = "This is an _itatlic_ paragraph"
        self.assertEqual(
            markdown_to_blocks(markdown),
            ["This is an _itatlic_ paragraph"]
        )

    def test_markdown_to_blocks_filters_empty_blocks(self):
        markdown = """
This set of blocks



has extra whitespace
        """
        self.assertEqual(
            markdown_to_blocks(markdown),
            [
                "This set of blocks",
                "has extra whitespace"
            ]
        )

    def test_markdown_to_blocks_strips_whitespace(self):
        markdown = "  This is a paragraph    "
        self.assertEqual(
            markdown_to_blocks(markdown),
            ["This is a paragraph"]
        )


if __name__ == "__main__":
    _ = unittest.main()

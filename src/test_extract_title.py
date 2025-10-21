import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        markdown = """
# This is the title

Here is a paragraph of text also on the page.
        """
        title = extract_title(markdown)
        self.assertEqual(
            title,
            "This is the title"
        )


    def test_title_is_first_if_multiple(self):
        markdown = """
# This is the title

# This should not be the title
        """
        title = extract_title(markdown)
        self.assertEqual(
            title,
            "This is the title"
        )

    def test_no_title_raises_value_error(self):
        markdown = """
This document has no title and should throw a value error
        """
        with self.assertRaises(ValueError):
            _ = extract_title(markdown)

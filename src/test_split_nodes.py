import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_single_char_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_multi_char_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_no_delimiters(self):
        node = TextNode("Plain text", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)

    def text_split_nodes_delimiter_unmatched_delimiter(self):
        node = TextNode("Unmatched _delimiters", TextType.PLAIN)
        with self.assertRaises(Exception):
            _ = split_nodes_delimiter([node], "_", TextType.ITALIC)

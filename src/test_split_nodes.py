import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestSplitNodes(unittest.TestCase):
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

    def test_split_nodes_delimiter_multiple_matches(self):
        node = TextNode("This is _text_ with _italics_", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.ITALIC),
            TextNode(" with ", TextType.PLAIN),
            TextNode("italics", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_multiple_inputs(self):
        nodes = [
            TextNode("This has no delimiters", TextType.PLAIN),
            TextNode("This is not plain text", TextType.BOLD),
            TextNode("This has _italic text_", TextType.PLAIN),
            TextNode("This is also _italic_", TextType.PLAIN),
        ]
        new_nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This has no delimiters", TextType.PLAIN),
            TextNode("This is not plain text", TextType.BOLD),
            TextNode("This has ", TextType.PLAIN),
            TextNode("italic text", TextType.ITALIC),
            TextNode("This is also ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_unmatched_delimiter(self):
        node = TextNode("Unmatched _delimiters", TextType.PLAIN)
        with self.assertRaises(Exception):
            _ = split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_split_nodes_image_match(self):
        node = TextNode("This is text with an ![alt text](https://example.com) image", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with an ", TextType.PLAIN),
            TextNode("alt text", TextType.IMAGE, "https://example.com"),
            TextNode(" image", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_image_multiple_matches(self):
        node = TextNode("This is ![1](https://example.com) text with two images ![2](https://example.com)", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("1", TextType.IMAGE, "https://example.com"),
            TextNode(" text with two images ", TextType.PLAIN),
            TextNode("2", TextType.IMAGE, "https://example.com"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_image_multiple_nodes(self):
        nodes = [
            TextNode("This is not plain text", TextType.BOLD),
            TextNode("![alt text](https://example.com) This has an image", TextType.PLAIN),
            TextNode("This has no image", TextType.PLAIN),
            TextNode("This also has an image ![alt text](https://example.com)", TextType.PLAIN),
        ]
        new_nodes = split_nodes_image(nodes)
        expected_nodes = [
            TextNode("This is not plain text", TextType.BOLD),
            TextNode("alt text", TextType.IMAGE, "https://example.com"),
            TextNode(" This has an image", TextType.PLAIN),
            TextNode("This has no image", TextType.PLAIN),
            TextNode("This also has an image ", TextType.PLAIN),
            TextNode("alt text", TextType.IMAGE, "https://example.com"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_image_no_matches(self):
        node = TextNode("This is text with no images", TextType.PLAIN)
        new_nodes = split_nodes_image([node])
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link_match(self):
        node = TextNode("This is text with a [click me](https://example.com) link", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("click me", TextType.LINK, "https://example.com"),
            TextNode(" link", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link_multiple_matches(self):
        node = TextNode("This is [click](https://example.com) text with two links [me](https://example.com)", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("click", TextType.LINK, "https://example.com"),
            TextNode(" text with two links ", TextType.PLAIN),
            TextNode("me", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link_multiple_nodes(self):
        nodes = [
            TextNode("This is not plain text", TextType.BOLD),
            TextNode("[this is a link](https://example.com)", TextType.PLAIN),
            TextNode("This has no link", TextType.PLAIN),
            TextNode("This has a link [click me](https://example.com)", TextType.PLAIN),
        ]
        new_nodes = split_nodes_link(nodes)
        expected_nodes = [
            TextNode("This is not plain text", TextType.BOLD),
            TextNode("this is a link", TextType.LINK, "https://example.com"),
            TextNode("This has no link", TextType.PLAIN),
            TextNode("This has a link ", TextType.PLAIN),
            TextNode("click me", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link_no_matches(self):
        node = TextNode("This is text with no links", TextType.PLAIN)
        new_nodes = split_nodes_link([node])
        expected_nodes = [node]
        self.assertEqual(new_nodes, expected_nodes)


if __name__ == "__main__":
    _ = unittest.main()

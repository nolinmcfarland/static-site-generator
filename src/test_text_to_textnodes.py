import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![alt text](https://example.com) and a [link](https://example.com)"
        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("alt text", TextType.IMAGE, "https://example.com"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]  
        self.assertEqual(
            text_to_textnodes(text),
            expected_nodes
        )


if __name__ == "__main__":
    _ = unittest.main()

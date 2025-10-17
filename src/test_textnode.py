import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_whenNotEqual(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a italic node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_withURL(self):
        node = TextNode("This is a link node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a link node", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)

    def test_eq_whenNoEqual_withDifferentURL(self):
        node = TextNode("This is a link node", TextType.LINK)
        node2 = TextNode("This is a link node", TextType.LINK, "https://example.com")
        self.assertNotEqual(node, node2)

    def test_to_html_node_text(self):
        text_node = TextNode("Plain text", TextType.PLAIN).to_html_node()
        html_node = HTMLNode(value="Plain text")
        self.assertEqual(text_node, html_node)

    def test_to_html_node_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD).to_html_node()
        html_node = HTMLNode("b", "Bold text")
        self.assertEqual(text_node, html_node)

    def test_to_html_node_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC).to_html_node()
        html_node = HTMLNode("i", "Italic text")
        self.assertEqual(text_node, html_node)

    def test_to_html_node_code(self):
        text_node = TextNode("Code snippet", TextType.CODE).to_html_node()
        html_node = HTMLNode("code", "Code snippet")
        self.assertEqual(text_node, html_node)

    def test_to_html_node_link(self):
        text_node = TextNode("Click me", TextType.LINK, "https://example.com").to_html_node()
        html_node = HTMLNode("a", "Click me", props={"href": "https://example.com"})
        self.assertEqual(text_node, html_node)

    def test_to_html_node_image(self):
        text_node = TextNode("Alt text", TextType.IMAGE, "https://example.com").to_html_node()
        html_node = HTMLNode("img", "", props={"src": "https://example.com", "alt": "Alt text"})
        self.assertEqual(text_node, html_node)


if __name__ == "__main__":
    _ = unittest.main()

import unittest
from textnode import TextNode, TextType


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


if __name__ == "__main__":
    _ = unittest.main()

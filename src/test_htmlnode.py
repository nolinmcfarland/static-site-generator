import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        expected_html = ' href="https://www.google.com" target="_blank"'
        actual_html = node.props_to_html()
        self.assertEqual(actual_html, expected_html)


if __name__ == "__main__":
    _ = unittest.main()

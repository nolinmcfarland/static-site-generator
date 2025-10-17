import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("p", "Paragraph")
        parent_node = ParentNode("div", [child_node], {"id": "some-id"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="some-id"><p>Paragraph</p></div>'
        )

    def test_to_html_with_child_props(self):
        child_node = LeafNode("p", "Classed paragraph", {"class": "some-class"})
        parent_node = ParentNode("div", [child_node], {"id": "some-id"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="some-id"><p class="some-class">Classed paragraph</p></div>'
        )


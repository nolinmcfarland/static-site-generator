import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        markdown = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",

        )

    def test_heading(self):
        markdown = """
# This is an H1

## This is an H2

### This is an H3

#### This is an H4

##### This is an H5

###### This is an H6
        """
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><h1>This is an H1</h1><h2>This is an H2</h2><h3>This is an H3</h3><h4>This is an H4</h4><h5>This is an H5</h5><h6>This is an H6</h6></div>"
        )

    def test_quote(self):
        markdown = """
>This is a
>block quote.
        """
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>This is a block quote.</blockquote></div>"
        )

    def test_unordered_list(self):
        markdown = """
- Apple
- Banana
- Cupcake
        """
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>Apple</li><li>Banana</li><li>Cupcake</li></ul></div>"
        )

    def test_ordered_list(self):
        markdown = """
1. Apple
2. Banana
3. Cupcake
        """
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>Apple</li><li>Banana</li><li>Cupcake</li></ol></div>"
        )


if __name__ == "__main__":
    _ = unittest.main()

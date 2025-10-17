from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag")
        if self.children is None:
            raise ValueError("no children")
        inner_html = "".join(
            list(
                map(
                    lambda node: node.to_html(),
                    self.children
                )
            )
        )
        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"

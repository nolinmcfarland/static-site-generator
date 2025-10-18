from textnode import TextNode, TextType


def split_nodes_delimiter(nodes, delimiter, text_type):
    new_nodes = []
    for node in nodes:
        if node.text_type is not TextType.PLAIN or delimiter not in node.text:
            new_nodes.append(node)
            continue
        delimiter_count = node.text.count(delimiter)
        if delimiter_count % 2 != 0:
            raise Exception("unmatched delimiter in node text")
        text_splits = node.text.split(delimiter)
        are_delimiters_even = node.text[0] == delimiter
        for i in range(0, len(text_splits)):
            text = text_splits[i]
            if (i % 2 == 0) == are_delimiters_even:
                new_nodes.append(TextNode(text, text_type))
            else:
                new_nodes.append(TextNode(text, node.text_type))
    return new_nodes


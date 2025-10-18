from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(nodes, delimiter, text_type):
    new_nodes = []
    for node in nodes:
        if node.text_type is not TextType.PLAIN or delimiter not in node.text:
            new_nodes.append(node)
            continue
        delimiter_count = node.text.count(delimiter)
        if delimiter_count % 2 != 0:
            raise Exception("unmatched delimiter")
        splits = node.text.split(delimiter)
        for i in range(0, len(splits)):
            text = splits[i]
            if text != "":
                if i % 2 == 0:
                    new_nodes.append(TextNode(text, TextType.PLAIN))
                else:
                    new_nodes.append(TextNode(text, text_type))
    return new_nodes

        
def split_nodes_image(nodes):
    new_nodes = []
    for node in nodes:
        if node.text_type is not TextType.PLAIN:
            new_nodes.append(node)
            continue
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        text = node.text
        for match in matches:
            markdown = f"![{match[0]}]({match[1]})"
            splits = text.split(markdown, maxsplit=1)
            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], TextType.PLAIN))
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            text = splits[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.PLAIN))
    return new_nodes


def split_nodes_link(nodes):
    new_nodes = []
    for node in nodes:
        if node.text_type is not TextType.PLAIN:
            new_nodes.append(node)
            continue
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        text = node.text
        for match in matches:
            markdown = f"[{match[0]}]({match[1]})"
            splits = text.split(markdown, maxsplit=1)
            if splits[0] != "":
                new_nodes.append(TextNode(splits[0], TextType.PLAIN))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            text = splits[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.PLAIN))
    return new_nodes

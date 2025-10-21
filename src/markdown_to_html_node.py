from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    child_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match (block_type):
            case BlockType.PARAGRAPH:
                child_nodes.append(__paragraph_to_html_node(block))
            case BlockType.HEADING:
                child_nodes.append(__heading_to_html_node(block))
            case BlockType.CODE:
                child_nodes.append(__code_to_html_node(block))
            case BlockType.QUOTE:
                child_nodes.append(__quote_to_html_node(block))
            case BlockType.UNORDERED_LIST:
                child_nodes.append(__unordered_list_to_html_node(block))
            case BlockType.ORDERED_LIST:
                child_nodes.append(__ordered_list_to_html_node(block))
    return ParentNode("div", child_nodes)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return list(
        map(
            lambda node: node.to_html_node(),
            text_nodes
        )
    )


def __paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

    
def __heading_to_html_node(block):
    level = 0
    for chr in block:
        if chr != "#" or level >= 6:
            break
        level += 1
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def __code_to_html_node(block):
    text = block[4:-3]
    text_node = TextNode(text, TextType.PLAIN)
    html_node = text_node.to_html_node()
    code = ParentNode("code", [html_node])
    return ParentNode("pre", [code])


def __quote_to_html_node(block):
    lines = list(
        map(
            lambda line: line[2:],
            block.split("\n")
        )
    )
    paragraph = " ".join(lines)
    children = text_to_children(paragraph) 
    return ParentNode("blockquote", children)


def __unordered_list_to_html_node(block):
    list_items = []
    for line in block.split("\n"):
        children = text_to_children(line[2:])
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)


def __ordered_list_to_html_node(block):
    list_items = []
    for line in block.split("\n"):
        children = text_to_children(line[3:])
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)



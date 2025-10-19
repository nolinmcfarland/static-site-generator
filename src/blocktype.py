from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    if __is_heading(block):
        return BlockType.HEADING
    elif __is_code(block):
        return BlockType.CODE
    elif __is_quote(block):
        return BlockType.QUOTE
    elif __is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif __is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    

def __is_heading(block):
    return re.match(r"^\#{1,6} ", block)


def __is_code(block):
    return block.startswith("```") and block.endswith("```")


def __is_quote(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True


def __is_unordered_list(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith("- "):
            return False
    return True


def __is_ordered_list(block):
    lines = block.split("\n")
    for i in range(0, len(lines)):
        if not re.match(f"^{i + 1}\\. ", lines[i]):
            return False
    return True

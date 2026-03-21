from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks]
    blocks = [block for block in blocks if block != ""]
    return blocks


def block_to_block_type(block):
    lines = block.split("\n")
    if lines[0].startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if lines[0].startswith("```") and lines[-1].startswith("```") and len(lines) >= 3:
        return BlockType.CODE
    
    for line in lines:
        if not line.startswith("- "):
            break
    else:
        return BlockType.UNORDERED_LIST
    
    for line in lines:
        if not line.startswith(">"):
            break
    else:
        return BlockType.QUOTE
    
    ordered_num = 1
    for line in lines:
        if not lines.startswith(f"{ordered_num}. "):
            break
        ordered_num += 1
    else:
        return BlockType.UNORDERED_LIST
    
    return BlockType.PARAGRAPH
    

    
    
    


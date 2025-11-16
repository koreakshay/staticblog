from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if lines[0].startswith("#"):
        header = lines[0]
        count = 0
        for c in header:
            if c == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and header[count:].startswith(" "):
            return BlockType.HEADING

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    is_ordered = True
    expected_num = 1
    for line in lines:
        prefix = f"{expected_num}. "
        if not line.startswith(prefix):
            is_ordered = False
            break
        expected_num += 1
    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
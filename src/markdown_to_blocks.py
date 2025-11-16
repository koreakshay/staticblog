def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")

    blocks = []
    for block in raw_blocks:
        stripped_block = block.strip()
        if not stripped_block:
            continue
        cleaned_lines = [line.strip() for line in stripped_block.split("\n")]
        cleaned = "\n".join(cleaned_lines)
        blocks.append(cleaned)

    return blocks
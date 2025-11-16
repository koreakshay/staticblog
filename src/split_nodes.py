from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only split plain text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        parts = text.split(delimiter)

        # If there is an uneven number of delimiter parts, syntax is invalid
        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax, missing closing delimiter '{delimiter}' in: {text}")

        # Rebuild nodes by alternating between text and the new type
        for index, part in enumerate(parts):
            if part == "":
                continue

            if index % 2 == 0:  # even index → normal text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:  # odd index → delimiter-wrapped content
                new_nodes.append(TextNode(part, text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        for alt, url in images:
            split_text = text.split(f"![{alt}]({url})", 1)
            before = split_text[0]
            after = split_text[1] if len(split_text) > 1 else ""

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            text = after

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        for anchor, url in links:
            split_text = text.split(f"[{anchor}]({url})", 1)
            before = split_text[0]
            after = split_text[1] if len(split_text) > 1 else ""

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(anchor, TextType.LINK, url))

            text = after

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
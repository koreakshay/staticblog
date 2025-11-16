from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link, split_nodes_delimiter

def text_to_textnodes(text):
    # Start with a single raw text node
    nodes = [TextNode(text, TextType.TEXT)]

    # Order matters: code → bold → italic → images → links
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    # Images before links
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

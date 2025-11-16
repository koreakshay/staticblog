from leafnode import LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise Exception("Input must be a TextNode")

    ttype = text_node.text_type

    if ttype == TextType.TEXT:
        return LeafNode(None, text_node.text)

    if ttype == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if ttype == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if ttype == TextType.CODE:
        return LeafNode("code", text_node.text)

    if ttype == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if ttype == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    raise Exception("Unknown TextType")
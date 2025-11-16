from markdown_to_blocks import markdown_to_blocks
from block_to_block import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from text_to_html import text_node_to_html_node
from leafnode import LeafNode

def text_to_children(text):
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in nodes]

def handle_paragraph(block):
    text = " ".join(block.split("\n"))
    p = HTMLNode("p", None, [])
    p.children = text_to_children(text)
    return p

def handle_heading(block):
    # count '#' prefix
    count = 0
    for c in block:
        if c == "#":
            count += 1
        else:
            break
    text = block[count+1:]
    h = HTMLNode(f"h{count}", None, [])
    h.children = text_to_children(text)
    return h

def handle_code(block):
    inner = block.strip("`")
    pre = HTMLNode("pre", None, [])
    code_node = LeafNode("code", inner)
    pre.children = [code_node]
    return pre

def handle_quote(block):
    lines = [line.lstrip("> ").rstrip() for line in block.split("\n")]
    combined = " ".join(lines)
    blockquote = HTMLNode("blockquote", None, [])
    blockquote.children = text_to_children(combined)
    return blockquote

def handle_unordered_list(block):
    items = block.split("\n")
    ul = HTMLNode("ul", None, [])
    children = []
    for line in items:
        text = line[2:]
        li = HTMLNode("li", None, [])
        li.children = text_to_children(text)
        children.append(li)
    ul.children = children
    return ul

def handle_ordered_list(block):
    items = block.split("\n")
    ol = HTMLNode("ol", None, [])
    children = []
    for line in items:
        # remove leading "1. ", "2. ", etc
        text = line.split(". ",1)[1]
        li = HTMLNode("li", None, [])
        li.children = text_to_children(text)
        children.append(li)
    ol.children = children
    return ol

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    root = HTMLNode("div", None, [])
    children = []

    for block in blocks:
        btype = block_to_block_type(block)

        if btype == BlockType.PARAGRAPH:
            children.append(handle_paragraph(block))
        elif btype == BlockType.HEADING:
            children.append(handle_heading(block))
        elif btype == BlockType.CODE:
            children.append(handle_code(block))
        elif btype == BlockType.QUOTE:
            children.append(handle_quote(block))
        elif btype == BlockType.UNORDERED_LIST:
            children.append(handle_unordered_list(block))
        elif btype == BlockType.ORDERED_LIST:
            children.append(handle_ordered_list(block))

    root.children = children
    return root
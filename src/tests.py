import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    # define test for HTMLNode class (at least 3 )
    def test_htmlnode_repr(self):
        from htmlnode import HTMLNode
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "greeting"})
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()

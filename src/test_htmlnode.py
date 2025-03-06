import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "text", "https://www.boot.dev",{
    "href": "https://www.google.com",
    "target": "_blank",
})
        node2 = HTMLNode("p", "text", "https://www.boot.dev",{
"href": "https://www.google.com",
"target": "_blank",
})
        self.assertEqual(node, node2)

        
def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()
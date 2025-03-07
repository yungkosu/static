from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    print(TextNode("This is some anchor text", "link", "https://www.boot.dev"))
    print(HTMLNode("a", "This is some anchor text", [], {
    "href": "https://www.google.com",
    "target": "_blank",
}))
    
main()
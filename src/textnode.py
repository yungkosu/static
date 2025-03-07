from enum import Enum

class TextType(Enum):
    TEXT="text"
    BOLD="bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None, src=None, alt=None):
        self.text = text
        self.text_type = text_type 
        self.url = url
        self.src = src
        self.alt = alt
    
    def __eq__(self, other):
        if isinstance(other, TextNode):
            if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
                return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text} {self.text_type} {self.url})"
    
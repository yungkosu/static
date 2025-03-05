from enum import Enum

class TextType(Enum):
    BOLD="**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode:
    def __init(self, text, url=None):
        self.text_type = super().__init__(TextType) 
        self.text = text
        self.url = url
    
    def __eq__(self, other):
        if isinstance(other, TextType):
            if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
                return True
    
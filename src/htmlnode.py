class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        props = ""
        for key, value in self.props.items():
            props += f' {key}="{value}"'
        return props
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
                return True
        return False
    

    def __repr__(self):
        return f"HTMLNode({self.tag} {self.value} {self.children} {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __eq__(self, other):
        if isinstance(other, LeafNode):
            if self.tag == other.tag and self.value == other.value and self.props == other.props:
                return True
        return False
    

class ParentNode(HTMLNode):
        def __init__(self, tag, children, props=None):
            super().__init__(tag, None, children, props)

        def to_html(self):
            if not self.tag:
                raise ValueError("Parent nodes must have a tag")
            if not self.children:
                raise ValueError("Parent nodes must have children")
            parent = ""
            for child in self.children:
                if not isinstance(child, HTMLNode):
                    raise ValueError("Not a valid HTML node")
                parent += f"{child.to_html()}"
            return f"<{self.tag}>{parent}</{self.tag}>"



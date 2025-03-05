class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props = ""
        for key, value in self.props.items():
            props += f' {key}=" {value}"'
        return props
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
                return True
        return False
    

    def __repr__(self):
        return f"HTMLNode({self.tag} {self.value} {self.children} {self.props})"
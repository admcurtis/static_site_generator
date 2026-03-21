class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string = ''
        if not self.props:
            return string
        for k, v in self.props.items():
            string += f' {k}="{v}"'
        return string

    
    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={self.children}, props={self.props})"
        )

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}"
        properties = self.props_to_html()
        if not properties:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{properties}>{self.value}</{self.tag}>'
        
    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"props={self.props})"
        )

      
class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("you must provide a tag value")
        if not self.children:
            raise ValueError("you must provide a children value")
        string = ""
        for child in self.children:
            string += child.to_html()
        string = f"<{self.tag}>{string}</{self.tag}>"
        return string

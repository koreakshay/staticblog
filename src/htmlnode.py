class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            return self.value or ""
        props_str = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children) if self.children else ""
        value_html = self.value or ""
        return f"<{self.tag}{props_str}>{value_html}{children_html}</{self.tag}>"
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return " " + props_str
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
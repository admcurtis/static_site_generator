import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_none(self):
        node = HTMLNode(tag="p", value="cat")
        self.assertEqual(node.props_to_html(), "")

    def test_one(self):
        node = HTMLNode(tag="p", value="cat", props={"class": "greeting"})
        self.assertEqual(node.props_to_html(), ' class="greeting"')

    def test_two(self):
        node = HTMLNode(tag="p", value="cat", props={"class": "greeting", "href": "404"})
        self.assertEqual(node.props_to_html(), ' class="greeting" href="404"')


class TestLeafNode(unittest.TestCase):
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Hello, world!", props={"href": "404"})
        self.assertEqual(node.to_html(), '<a href="404">Hello, world!</a>')

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )



if __name__ == "__main__":
    unittest.main()
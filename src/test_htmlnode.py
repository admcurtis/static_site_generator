import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
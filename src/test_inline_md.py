from inline_md import (
    split_nodes_delimiter, extract_markdown_images, extract_markdown_links,
    split_nodes_image, split_nodes_link, text_to_textnodes
)
from textnode import TextNode, TextType
import unittest

class TestSpliiter(unittest.TestCase):

    def test_basic(self):
        node = TextNode("This is a `code` node", TextType.TEXT)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" node", TextType.TEXT)
        ]
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.CODE),
            expected
        )

    def test_multiple_blocks(self):
        node = TextNode("This is a multi **bold** node **bold**", TextType.TEXT)
        expected = [
            TextNode("This is a multi ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" node ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            expected
        )

    def test_multiple_nodes(self):
        nodes = [
            TextNode("This is a multi **bold** node **bold**", TextType.TEXT),
            TextNode("Not a text node, its italic", TextType.ITALIC)
        ]
        expected = [
            TextNode("This is a multi ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" node ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("Not a text node, its italic", TextType.ITALIC)
        ]
        self.assertEqual(
            split_nodes_delimiter(nodes, "**", TextType.BOLD),
            expected
        )

    def test_no_closing_delimiter(self):
        node = TextNode("This is a `code node", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    # Test to_textnode function
    def test_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_nodes, expected)



class TestExtractImage(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_no_link(self):
        matches = extract_markdown_images(
            "This is text with no image"
        )
        self.assertListEqual([], matches)

    

class TestExtractLink(unittest.TestCase):


    def test_extract_markdown_images_no_link(self):
        matches = extract_markdown_images(
            "Here is a link [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [("to youtube", "https://www.youtube.com/@bootdotdev")],
            matches
        )

    def test_extract_markdown_images_no_link(self):
        matches = extract_markdown_images(
            "Here is a link is not!"
        )
        self.assertListEqual(
            [],
            matches
        )

class TestSplitLinkImage(unittest.TestCase):

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://wikipedia.org"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
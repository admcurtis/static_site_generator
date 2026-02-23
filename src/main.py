from textnode import TextNode, TextType


def main():
    some_text = TextNode("hello world", TextType.BOLD, None)
    print(some_text)

if __name__ == "__main__":
    main()
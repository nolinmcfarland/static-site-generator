from textnode import TextNode, TextType


def main():
    node = TextNode('print("hello world")', TextType.CODE, None)
    print(node)


if __name__ == "__main__":
    main()

import re


def extract_title(markdown):
    pattern = r"^\# (.*?)$"
    match = re.search(pattern, markdown, flags=re.MULTILINE)
    if match is None:
        raise ValueError("markdown must include an H1")
    return match[1]

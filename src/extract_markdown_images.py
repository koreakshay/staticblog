import re

IMAGE_PATTERN = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
LINK_PATTERN = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

def extract_markdown_images(text):
    matches = re.findall(IMAGE_PATTERN, text)
    return [(alt, url) for alt, url in matches]

def extract_markdown_links(text):
    matches = re.findall(LINK_PATTERN, text)
    return [(anchor, url) for anchor, url in matches]
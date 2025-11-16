"""Generate an HTML page from markdown using an HTML template."""

import os

from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str = "/") -> None:
    """Generate a single HTML page.

    - from_path: path to the source markdown file
    - template_path: path to the HTML template file
    - dest_path: path where the rendered HTML file should be written
    """
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}"
    )

    # Read markdown source
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    # Read HTML template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    # Extract title from markdown
    title = extract_title(markdown)

    # Replace placeholders in template
    full_html = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content)
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    # Ensure destination directory exists
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    # Write final HTML to destination
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)

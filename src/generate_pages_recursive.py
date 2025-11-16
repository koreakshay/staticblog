

"""Recursively generate HTML pages from markdown content."""

import os

from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """Recursively walk dir_path_content and generate HTML files in dest_dir_path.

    For each .md file found under dir_path_content, generate a corresponding
    .html file in the mirrored path under dest_dir_path using the given
    template_path.
    """
    # Ensure destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)

    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)
        dst_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(src_path):
            # Recurse into subdirectory, mirroring structure under dest_dir_path
            generate_pages_recursive(src_path, template_path, dst_path)
        elif os.path.isfile(src_path) and entry.lower().endswith(".md"):
            # Map markdown file to .html in destination
            html_dst = os.path.splitext(dst_path)[0] + ".html"
            generate_page(src_path, template_path, html_dst)
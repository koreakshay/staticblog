import os
import shutil

from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive


def copy_dir(src, dst):
    os.makedirs(dst, exist_ok=True)

    for name in os.listdir(src):
        src_path = os.path.join(src, name)
        dst_path = os.path.join(dst, name)

        if os.path.isdir(src_path):
            copy_dir(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)
            print(f"Copied {src_path} -> {dst_path}")


def copy_static(src="static", dst="public"):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    copy_dir(src, dst)


def main():
    # Copy static assets into public/
    copy_static("static", "public")
    # Generate pages for all markdown files under content/
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
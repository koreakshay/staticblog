import os
import shutil
import sys

from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

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


def copy_static(src="static", dst="docs"):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    copy_dir(src, dst)


def main():
    copy_static("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
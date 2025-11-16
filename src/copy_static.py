import os
import shutil

def copy_dir(src, dst):
    """Recursively copy all files and subdirectories from src to dst."""
    os.makedirs(dst, exist_ok=True)

    for name in os.listdir(src):
        src_path = os.path.join(src, name)
        dst_path = os.path.join(dst, name)

        if os.path.isdir(src_path):
            # Recurse into subdirectory
            copy_dir(src_path, dst_path)
        else:
            # Copy file
            shutil.copy(src_path, dst_path)
            print(f"Copied {src_path} -> {dst_path}")

def copy_static(src="static", dst="public"):
    """Delete dst if it exists, then recursively copy src into dst."""
    if os.path.exists(dst):
        shutil.rmtree(dst)
    copy_dir(src, dst)
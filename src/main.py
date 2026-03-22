import os
import shutil
from gencontent import extract_title, generate_page

def main():

    dst = "./public"
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    os.mkdir(dst)

    src = "./static"
    copy_dir(src, dst)

    generate_page("./content/index.md", "template.html", "./public/index.html")


def copy_dir(src, dst):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"copying: {src_path}")
            shutil.copy(src_path, dst_path)
        else:
            os.mkdir(dst_path)
            copy_dir(src_path, dst_path)



if __name__ == "__main__":
    main()
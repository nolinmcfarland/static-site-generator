import os
import shutil
from generate_page import generate_pages


def main():
    template = "./template.html"
    static = "./static"
    content = "./content"
    public = "./public"

    if not os.path.exists(static):
        raise Exception(f"source does not exist at {static}")

    if os.path.exists(public):
        print(f"Removing directory {public}")
        remove_path(public)

    copy_path(static, public)
    generate_pages(content, template, public)



def remove_path(path):
    if os.path.isfile(path):
        os.remove(path)
    else:
        for subpath in os.listdir(path):
            remove_path(os.path.join(path, subpath))
        os.rmdir(path)


def copy_path(path, destination):
    if os.path.isfile(path):
        print(f"Copying file from {path} to {destination}")
        shutil.copy(path, destination)
    else:
        if not os.path.exists(destination):
            print(f"Making directory {destination}")
            os.mkdir(destination)
        for subpath in os.listdir(path):
            copy_path(
                os.path.join(path, subpath),
                os.path.join(destination, subpath)
            )


if __name__ == "__main__":
    main()

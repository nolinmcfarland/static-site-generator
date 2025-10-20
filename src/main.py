import os
import shutil


def main():
    source = "./static"
    destination = "./public"
    if not os.path.exists(source):
        raise Exception(f"source does not exist at {source}")
    if os.path.exists(destination):
        print(f"Removing directory {destination}")
        remove_path(destination)
    copy_path(source, destination)


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

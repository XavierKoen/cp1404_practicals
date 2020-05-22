"""Sort files by extension as subdirectories."""
import os
import shutil


def main():
    """Sorts files into subdirectories created based on extensions"""
    os.chdir("FilesToSort")
    files = os.listdir('.')
    for file in files:
        extension = file[file.find('.') + 1:]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(file, extension)


main()

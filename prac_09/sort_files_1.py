"""Sort files by extension as subdirectories."""
import os
import shutil


def main():
    """Sorts files into subdirectories created based on extensions"""
    os.chdir("FilesToSort")
    files = os.listdir('.')
    for file in files:
        extension_directory = file[file.find('.') + 1:]
        try:
            os.mkdir(extension_directory)
        except FileExistsError:
            pass
        shutil.move(file, extension_directory)


main()

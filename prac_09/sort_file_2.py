"""Sort files based on user input categories as subdirectories."""
import os
import shutil


def main():
    """Sorts files into subdirectories created based on user input"""
    os.chdir("FilesToSort")
    files = os.listdir('.')
    extension_to_directory = {}
    for file in files:
        extension = file[file.find('.') + 1:]
        if extension not in extension_to_directory:
            directory = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_directory[extension] = directory
        try:
            os.mkdir(extension_to_directory[extension])
        except FileExistsError:
            pass


main()

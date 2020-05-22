"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_filename = ''
    skip_next_char = False
    for i, char in enumerate(filename, 0):
        if skip_next_char:
            skip_next_char = False
            pass
        elif char == ' ':
            next_char_upper = filename[i + 1].upper()
            new_filename = new_filename + ' ' + next_char_upper
            skip_next_char = True
        else:
            new_filename += char
    new_name = new_filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # for filename in filenames:
        for filename in filenames:
            full_filename = os.path.join(directory_name, filename)
            new_filename = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_filename, new_filename)


# main()
demo_walk()

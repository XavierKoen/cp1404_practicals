"""
CP1404/CP5632 - Practical
Password checker code
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH,))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: {}".format(SPECIAL_CHARACTERS))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    """Determine if the provided password is valid."""

    # Establish counter variables.
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    # If length is wrong, return False.
    if MIN_LENGTH <= len(password) <= MAX_LENGTH:
        # Count each character using str methods.
        for char in password:
            count_lower = count_lower + int(char.islower())
            count_upper = count_upper + int(char.isupper())
            count_digit = count_digit + int(char.isdigit())
        # Return False if any are zero.
        if count_lower == 0 or count_upper == 0 or count_digit == 0:
            return False
        else:
            # Count special characters from SPECIAL_CHARACTERS string if required.
            # Return False if count_special is zero.
            if SPECIAL_CHARS_REQUIRED:
                for char in password:
                    count_special = count_special + int(char in SPECIAL_CHARACTERS)
                if count_special == 0:
                    return False
    else:
        return False

    # If we get here (without returning False), then the password must be valid.
    return True


main()

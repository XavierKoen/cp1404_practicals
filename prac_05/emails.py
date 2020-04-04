"""
Stores users' emails along with name associated with email address as a dictionary.
Continues to prompt user to input email addresses and names until blank input is received.
Prints names and emails after all emails have been stored.
"""


def main():
    """
    Prompt user for email input.
    Store email and name as dictionary.
    Return all names with respective emails.
    """
    email_address = input("Email: ")
    name = identify_name(email_address)
    print(name, email_address)  # Print to test if working.


def identify_name(email_address):
    """
    Check email address and acquires name of users' email.
    Allow for manual name correction if desired.
    """
    email_split_at_name = email_address.split('@')  # Split the email string into a list, with the user name section as
    # the first element and the rest of the address as the second (removing the @ symbol).
    name = ' '.join(email_split_at_name[0].split('.')).title()  # Replace potential '.' with ' ' within name and
    # capitalise name.
    is_name_correct = input("Is {} your name? (Y/n) ".format(name)).lower()  # Allow user to check if name is correct.
    if is_name_correct in ['no', 'n']:
        name = input("Name: ")
    return name


main()

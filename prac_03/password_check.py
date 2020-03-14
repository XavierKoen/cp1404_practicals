"""
Checks password character length to see if >= MINIMUM_LENGTH then displays length of password in asterisks (*).
"""

MINIMUM_LENGTH = 7

password = input("Please enter a password at least {} characters long: ".format(MINIMUM_LENGTH))
password_length = len(password)

while MINIMUM_LENGTH > password_length:
    password = input("Invalid password! Please enter a password of at least {} characters long: ".format(MINIMUM_LENGTH))
    password_length = len(password)

hidden_password = ""

for char in password:
    hidden_password = hidden_password + "*"

print(hidden_password)

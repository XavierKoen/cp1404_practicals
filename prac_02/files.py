"""
Do-from-scratch Exercises: Files section
The 4 different tasks are outlined in blocks of code.
"""

# User enters name, which is written into name.txt file.
name = input("Please enter name: ")
out_file_name = open("name.txt", "w")
print(name, file=out_file_name)
out_file_name.close()

# name.txt is opened and read, printing the line with string formatting.
in_file_name = open("name.txt", "r")
print("Your name is {}".format(in_file_name.read()))
in_file_name.close()

# numbers.txt is opened and read, calculating the addition of line 1 and 2 as integers.
# Result is printed.
in_file_numbers = open("numbers.txt", "r")
line1 = int(in_file_numbers.readline())
line2 = int(in_file_numbers.readline())
result = (line1 + line2)
print(result)
in_file_numbers.close()

# numbers.txt is opened and read, while the total for all lines is calculated and printed
# as floating point numbers.
in_file_numbers = open("numbers.txt", "r")
total = 0
i = 0
for line in in_file_numbers:
    total = total + float(line)
print(total)

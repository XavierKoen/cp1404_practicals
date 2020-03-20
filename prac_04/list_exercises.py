"""
User inputs 5 numbers, then the first number, last number,
smallest number, largest number and the average of the 5 numbers are displayed.
"""

NUMBER_OF_NUMBERS = 5
number = []
for i in range(1, NUMBER_OF_NUMBERS + 1):
    number.append(int(input("Number: ")))
print("The first number is {}".format(number[0]))
print("The last number is {}".format(number[NUMBER_OF_NUMBERS - 1]))
print("The smallest number is {}".format(min(number)))
print("The largest number is {}".format(max(number)))
total = sum(number)
print("The average of the numbers is {:.2f}".format(total/NUMBER_OF_NUMBERS))

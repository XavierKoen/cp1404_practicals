"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Please enter a non-zero denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
1. "When will a ValueError occur?"
    When the user enters anything into the numerator or denominator that is not an integer.

2. "When will a ZeroDivisionError occur?"
    When the user enters 0 into the denominator when prompted.

3. "Could you change the code to avoid the possibility of a ZeroDivisionError?"
    Yes, by adding a while loop to ask for a different denominator until a non-zero input is received.
"""
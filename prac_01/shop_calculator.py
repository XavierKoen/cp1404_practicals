"""
Program to calculate and display a user's total price of items based on each individual item's price.
User inputs number of items (0 or more) and inputs corresponding price of each item as prompted.
If invalid number of items input, then user will be asked to re-enter a valid number (>=0).
If the total price is over $100, then a 10% discount is applied to the total before being displayed.
"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    number_of_items = int(input("Invalid number of items! Please enter valid number of items: "))
total_price = 0
for i in range(1,number_of_items + 1):
    total_price = float(input("Price of item " + str(i) + ": $")) + total_price
if total_price > 100:
    total_price = total_price * 0.9
print("Total price for " + str(number_of_items) + " items ${:.2f}".format(total_price))
"""
Asks user for number of quick picks, then produces the desired number of quick picks.
"""

SMALLEST_NUMBER = 1
LARGEST_NUMBER = 45
LOTTERY_NUMBERS = 6
import random


def main():
    number_quick_picks = int(input("How many quick picks? "))
    generate_quick_picks(number_quick_picks)


def generate_quick_picks(number_of_picks):
    for pick in range(0, number_of_picks):  # repeat single pick code for as many iterations input
        a_pick = []  # initialise empty list for a single pick
        quick_pick_string_formatting = ""  # initialise string for presentable quick pick formatting
        while len(a_pick) < LOTTERY_NUMBERS:  # check to see if the pick has enough numbers
            number = random.randint(SMALLEST_NUMBER, LARGEST_NUMBER)
            if number not in a_pick:
                a_pick.append(number)
                quick_pick_string_formatting += "{:2} "  # add a position to the presentable quick pick formatting
            a_pick.sort()
        print(quick_pick_string_formatting.format(a_pick[0], a_pick[1], a_pick[2], a_pick[3], a_pick[4], a_pick[5]))
        # adjust number of a_pick indexing manually if adjusting LOTTERY_NUMBERS value respectively


main()

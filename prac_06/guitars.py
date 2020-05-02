"""
Program to store information on all of the user's guitars.
"""

from prac_06.guitar import Guitar


def main():
    """
    User continually prompted to input guitar make and model name, year of manufacturing, and cost until a blank name is
    entered.
    Information for each guitar is stored as an instance of the Guitar class.
    Each guitar instance is stored as a list of all guitars.
    Displays all guitar information nicely formatted, including whether vintage or not (50 years old or more).
    Vintage state is determined by Guitar class method .is_vintage.
    """
    print("My Guitars!")
    my_guitars = []
    name = input("Name: ")
    while name != '':
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        my_guitars.append(new_guitar)
        print("{} ({}) : ${} added.".format(name, year, cost))
        name = input("Name: ")
    print("\n...snip...\n")
    print("These are my guitars:")
    for i, guitar in enumerate(my_guitars):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))

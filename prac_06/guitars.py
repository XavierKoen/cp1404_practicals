"""

"""

from prac_06.guitar import Guitar

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

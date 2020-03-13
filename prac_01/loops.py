"""
Programs to display different kinds of lists (numerical and other).
"""

#Basic list of odd numbers between 1 and 20 (inclusive).
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#Section a: List counting in 10s from 0 to 100.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#Section b: List counting down from 20 to 1.
for i in range(1, 21):
    j = 21 - i
    print(j, end=' ')
print()

#Section c: Print number of stars (*) desired on one line.
number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    print("*",end="")
print()

#Section d: Print desired number of lines of stars (*) with increasing number of stars in each line.
#           Beginning with one and finishing with desired number.
number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    for j in range(1, i + 1):
        print("*",end="")
    print()
print()
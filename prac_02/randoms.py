"""
"What did you see on line 1?"
A random integer was printed between 5 and 20 inclusively,
5 being the smallest number I saw and 20 being the largest number I saw.

"What did you see on line 2?"
A random odd integer was printed between 3 and 10,
3 being the smallest number I saw and 9 being the largest number I saw.
Line 2 could not have produced a 4 as the integers were in intervals of 2 beginning at 3,
meaning no even numbers were possible.

"What did you see on line 3?"
A random floating point number was printed between 2.5 and 5.5 (possibly with a maximum decimal place of 16).
I am unsure of whether the numbers are 2.5 and/or 5.5 inclusive.
2.5065540414666017 was the smallest number I saw and 5.405390467109466 was the largest number I saw.

"""

import random
print(random.randint(1, 100))

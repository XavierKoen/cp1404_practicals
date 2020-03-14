"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)
    print(random_score())


def random_score():
    score = evaluate_score(random.uniform(0, 100))  # generates random floating point number between 0 and 100 inclusive
    return score


def evaluate_score(score):
    if 100 >= score >= 90:
        result = "Excellent"
    elif 90 > score >= 50:
        result = "Passable"
    elif 50 > score >= 0:
        result = "Bad"
    else:
        result = "Invalid score"
    return result


main()

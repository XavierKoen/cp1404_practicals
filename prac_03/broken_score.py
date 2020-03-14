"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)


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

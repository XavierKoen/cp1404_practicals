"""
Counts the number of word occurrences in the string input by user.
Returns each individual word in string with number of occurrences.
"""


def main():
    """
    String is turned into list of words to be 'counted'.
    The counted results are received and displayed.
    """
    list_of_words = input("Text: ").split()  # Turns string into list of words.
    print(word_occurrence_counter(list_of_words))  # Print received dictionary as test.


def word_occurrence_counter(words):
    """
    Counts occurrences of the same strings in a list.
    Returns count as a dictionary.
    """
    word_occurrence_dict = {}
    for word in words:
        try:
            word_occurrence_dict[word] += 1  # Add count to value of the word if this key exists.
        except KeyError:
            word_occurrence_dict[word] = 1  # Create key for unknown word and give value of 1.
    return word_occurrence_dict


main()

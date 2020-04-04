"""
Counts the number of word occurrences in the string input by user.
Returns each individual word alphabetically in string with number of occurrences.
"""


def main():
    """
    String is turned into list of words to be 'counted'.
    """
    list_of_words = input("Text: ").split()  # Turns string into list of words.
    word_occurrence_dict = word_occurrence_counter(list_of_words)
    output_alphabetically(word_occurrence_dict)


def output_alphabetically(word_occurrence_dict):
    """
    Word occurrence dictionary printed alphabetically.
    """
    words_alphabetical = sorted(word_occurrence_dict)  # Create alphabetical list of keys in word occurrence dictionary.
    number_formatting_spaces = find_longest_word_length(words_alphabetical)  # Acquire longest length required for
    # column spacing.
    for word in words_alphabetical:
        print("{:{}} : {}".format(word, number_formatting_spaces, word_occurrence_dict[word]))  # Print words from
        # alphabetical list and
        # respective occurrence count with neat column formatting.


def find_longest_word_length(words):
    """
    Find character length of longest word in words list.
    """
    word_length_list = []  # Initialise list for character length of all words.
    for word in words:
        word_length_list.append(len(word))  # Add length of word to list.
    return max(word_length_list)  # Return length of word with most characters.


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

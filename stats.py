def count_words(text: str):
    """
    Split string in a list and return the number of words in this list.
    """
    word_list = text.split()
    count = len(word_list)

    return count


def count_characters(text: str):
    """
    Count how many times each character appears in a string, and return the
    result as a dictionary.
    Return dict is structured this way:
    {"char1": "nb_char1", "char2": "nb_char2"...}.
    """
    char_count_dict = {}
    for c in text:
        c = c.lower()
        if c not in char_count_dict:
            char_count_dict[c] = 1
        else:
            char_count_dict[c] += 1

    sorted_dict = dict(
        sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)
    )

    return sorted_dict

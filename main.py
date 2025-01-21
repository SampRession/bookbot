"""
Here is the main.py docstring.
"""


def read_content(book: str):
    """
    Read content of a text file and store it in a variable, then return it.
    """
    with open(f"books/{book}.txt", encoding="utf8") as f:
        file_content = f.read()

        return file_content


def count_words(text: str):
    """
    Split string in a list and return the number of words in this list.
    """
    word_list = text.split()
    count = len(word_list)

    return count


def count_characters(text: str):
    """
    Count how many times each character appears in a string, and return the result as a dictionary.
    Return dict is structured this way: {"char1": "nb_char1", "char2": "nb_char2"...}.
    """
    char_count_dict = {}
    for c in text:
        c = c.lower()
        if not c in char_count_dict:
            char_count_dict[c] = 1
        else:
            char_count_dict[c] += 1

    sorted_dict = dict(
        sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)
    )

    return sorted_dict


def generate_report(book: str, count: int, char_dict: dict):
    """
    Generate and return a complete report about the text.
    This report contains total words count and individual character occurrences.
    """
    # sorted_dict = sorted(char_dict, key=char_dict.get)
    total_string = generate_char_report_string(char_dict)

    report = f"""
--- START Report of books/{book}.txt ---
{count} words found in the document.

{total_string}

--- Report END ---
    """

    print(report)


def generate_char_report_string(char_dict: dict):
    """
    Return a list containing an one-line string for each alpha character.
    """
    string_list = []
    total_string = ""
    for char in char_dict:
        if char.isalpha():
            char_string = (
                f"The '{char}' character was found {char_dict.get(char)} times"
            )
            string_list.append(char_string)

    for s in string_list:
        total_string += s + "\n"

    return total_string


def main():
    """
    Main function for bookbot program
    """
    book = "frankenstein"
    content = read_content(book)
    count = count_words(content)
    char_count_dict = count_characters(content)
    generate_report(book, count, char_count_dict)
    # dict_to_list(char_count_dict)


if __name__ == "__main__":
    main()

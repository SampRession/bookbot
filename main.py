import sys

from stats import count_characters, count_words


def read_content(book: str):
    """
    Read content of a text file and store it in a variable, then return it.
    """
    with open(book, encoding="utf8") as f:
        file_content = f.read()

        return file_content


def generate_report(book: str, count: int, char_dict: dict):
    """
    Generate and return a complete report about the text.
    This report contains total words count and individual
    character occurrences.
    """
    # sorted_dict = sorted(char_dict, key=char_dict.get)
    total_string = generate_char_report_string(char_dict)

    report = f"""
========== BOOKBOT ==========
Analyzing book found at books/{book}

--------- Word Count --------
{count} words found in the document.

------ Character Count ------
{total_string}

============ END ============
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
            char_string = f"{char}: {char_dict.get(char)}"
            string_list.append(char_string)

    for s in string_list:
        total_string += s + "\n"

    return total_string


def main():
    """
    Main function for bookbot program
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    content = read_content(book)
    count = count_words(content)
    char_count_dict = count_characters(content)
    generate_report(book, count, char_count_dict)


if __name__ == "__main__":
    main()

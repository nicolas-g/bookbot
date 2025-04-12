import sys
from stats import get_num_words, get_chars_dict, get_sorted_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        # books/frankenstein.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    contents = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    num_words = get_num_words(contents)
    print(f"Found {num_words} total words")

    # print(get_chars_dict(contents))
    chars_dict = get_chars_dict(contents)

    print("--------- Character Count -------")  # print(char_list.sort())
    sorted_chars_dict = get_sorted_dict(chars_dict)
    for i in sorted_chars_dict:
        print(i["char"] + ": " + str(i["count"]))
    print("============= END ===============")


if __name__ == "__main__":
    main()

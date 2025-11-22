import sys

from stats import get_character_counts, get_num_words, get_sorted_list_of_dicts


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    num_words = get_num_words(get_book_text(file_path))
    print(f"Found {num_words} total words.")

    character_counts = get_character_counts(get_book_text(file_path))

    sorted_dictionaries = get_sorted_list_of_dicts(character_counts)
    for dictionary in sorted_dictionaries:
        if dictionary["char"].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")


if __name__ == "__main__":
    main()

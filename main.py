from stats import get_word_count
from stats import get_letter_count
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_word_count(book_text)
    #print(book_text)

    letter_counts = get_letter_count(book_text)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Letter Counts ---------")
    #print(letter_counts)
    for letter in letter_counts:
        print(letter + ": " + str(letter_counts[letter]))
main()
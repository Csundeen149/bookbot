import sys
from stats import get_num_words, get_num_letters, sort_book

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Must have two arguments")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    num_words = get_num_words(get_book_text(book_path))
    num_letters = get_num_letters(get_book_text(book_path))
    items = sort_book(num_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in items:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")


### Run program
main()
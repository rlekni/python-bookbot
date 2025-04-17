from stats import count_words
from stats import count_chars
from stats import sort_results
import sys

def get_book_text(relative_path):
    file_contents = ""
    with open(relative_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path = args[1]
    print("============ BOOKBOT ============")
    # relative_path = "books/frankenstein.txt"
    file_contents = get_book_text(relative_path)
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    word_count = count_words(file_contents)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_count = count_chars(file_contents)
    # print(char_count)
    sorted_results = sort_results(char_count)
    # print(sorted_results)
    for result in sorted_results:
        char = result["char"]
        count = result["count"]
        if char.isalpha() == True:
            print(f"{char}: {count}")
    print("============= END ===============")

main()

def get_book_text(relative_path):
    file_contents = ""
    with open(relative_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(contents):
    split_words = contents.split()
    return len(split_words)


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    # print(file_contents)
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")


main()

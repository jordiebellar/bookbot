from stats import get_num_words
from stats import get_book_text

def main():
       file_contents = get_book_text("books/frankenstein.txt")
       word_count = get_num_words(file_contents)
       print(f"Found {word_count} total words")

main()
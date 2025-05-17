import sys
from stats import n_words, get_chars_dict, sort_dict

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Ffile not found at {book_path}")
        sys.exit(1)

    text = get_book_text(book_path)
    num_count =  n_words(text)
    chars_dict = get_chars_dict(text)
    report_list = sort_dict(chars_dict)


    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_count} total words")
    print("--------- Character Count -------")
    for char, count in report_list:
        print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()

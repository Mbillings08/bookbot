def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    try:
        book_filepath = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_filepath}...")
    
        from stats import get_num_words
    
        from stats import get_char_count
        print("============= END ===============")

    except FileNotFoundError:
        print(f"The file '{book_filepath}' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")
main()
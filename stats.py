def get_num_words():
       
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            wordcount = len(words)
            print(f"Total number of words: {wordcount}")
    except FileNotFoundError:
        print("The file 'books/frankenstein.txt' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")
get_num_words()
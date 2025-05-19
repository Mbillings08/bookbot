def get_num_words():
       
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            wordcount = len(words)
            print(f"{wordcount} words found in the document")

    except FileNotFoundError:
        print("The file 'books/frankenstein.txt' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")

get_num_words()


def get_char_count():
    t = 0
    p = 0
    c = 0
    characters = []
    try:
        with open("books/frankenstein.txt") as l:
            for line in l:
                for char in line:
                    characters.append(char)
        for letter in characters:
            lower_letter = letter.lower()
            if lower_letter == "t":
                t += 1
            if lower_letter == "p":
                p += 1
            if lower_letter == "c":
                c += 1
        #print(characters)
        print(f"'t': {t}")
        print(f"'p': {p}")
        print(f"'c': {c}")
                

            

    except FileNotFoundError:
        print("The file 'books/frankenstein.txt' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")       
get_char_count()

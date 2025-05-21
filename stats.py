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
    
    characters = []
    lower_characters = []
    results = []
    a_count = 0
    b_count = 0
    try:
        with open("books/frankenstein.txt") as l:
            for line in l:
                for char in line:
                    characters.append(char)
        for letter in characters:
            lower_letter = letter.lower()
            lower_is_alpha = lower_letter.isalpha()
            if lower_is_alpha is True:
                lower_characters.append(lower_letter)

        for l in lower_characters:
            if l == "a":
                a_count += 1
            if l == "b":
                b_count += 1
        print(a_count, b_count)
        
            #results + [f"{l}: {l_count}"]
        
        
        #print(results)

                
                
        
                

            

    except FileNotFoundError:
        print("The file 'books/frankenstein.txt' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")       
get_char_count()

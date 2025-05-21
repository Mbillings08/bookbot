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
    unique_characters = []
    results = []
    count = 0
    
    try:
        #open file and turn each character into list
        with open("books/frankenstein.txt") as l:
            for line in l:
                for char in line:
                    characters.append(char)

        #Turn list of characters all lower case
        for letter in characters:
            lower_letter = letter.lower()
            lower_is_alpha = lower_letter.isalpha()
            if lower_is_alpha is True:
                lower_characters.append(lower_letter)

        #get unique lowercase characters
        for lower_character in lower_characters:
            if lower_character not in unique_characters:
                unique_characters.append(lower_character)
        #print(unique_characters)

        #get counts for each unique character
        for u in unique_characters:
            count = lower_characters.count(u)
            results.append(f"{u}: {count}")

        
        print(results)

            #results + [f"{l}: {l_count}"]
        
        
        #print(results)

                
                
        
                

            

    except FileNotFoundError:
        print("The file 'books/frankenstein.txt' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")       
get_char_count()

def get_num_words():
    import sys
    book_filepath = sys.argv[1]
    print("--------- Word Count -------")
    try:
        
        with open(book_filepath) as f:
            file_contents = f.read()
            words = file_contents.split()
            wordcount = len(words)
            print(f"Found {wordcount} total words")

    except FileNotFoundError:
        print(f"The file '{book_filepath}' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")

get_num_words()


def get_char_count():
    import sys
    book_filepath = sys.argv[1]
    characters = []
    lower_characters = []
    unique_characters = []
    results = {}
    count = 0
    print("--------- Character Count -------")
    try:
        
        #open file and turn each character into list
        with open(book_filepath) as l:
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

        #get counts for each unique character and output to library
        for u in unique_characters:
            count = lower_characters.count(u)
            results[u] = count

        #organize result library by counts, high to low

        sorted_dict = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

        #return each value as it's own line
        for value in sorted_dict:
            print(f"'{value}: {sorted_dict[value]}") 

    except FileNotFoundError:
        print(f"The file '{book_filepath}' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")       
get_char_count()

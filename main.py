def main():
    file_contents = ""
    a_count = 0
    b_count = 0
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            wordcount = len(words)
            print(f"Total number of words: {wordcount}")

            lower_file_contents = file_contents.lower()
            lettercount = 0
            letter_totals = []
            for char in lower_file_contents:
                if char.isalpha():
                    lettercount += 1
                    letter_totals.append(char)
                    for letter in letter_totals:
                        if letter == "a":
                            a_count += 1
                        if letter == "b":
                            b_count += 1

                            
            print(letter_totals)
            print(lettercount)
            print(f"A count: {a_count}")
            print(f"A count: {b_count}")

            

    except FileNotFoundError:
        print("The file 'books/frankenstein.txt' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")
        
main()
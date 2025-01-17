def main():
    file_contents = ""
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
            print(lettercount)

    except FileNotFoundError:
        print("The file 'books/frankenstein.txt' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")
        
main()
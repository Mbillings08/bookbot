def main():
    file_contents = ""
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    f_count = 0
    g_count = 0
    h_count = 0
    i_count = 0
    j_count = 0
    k_count = 0
    l_count = 0
    m_count = 0
    n_count = 0
    o_count = 0
    p_count = 0
    q_count = 0
    r_count = 0
    s_count = 0
    t_count = 0
    u_count = 0
    v_count = 0
    w_count = 0
    x_count = 0
    y_count = 0
    z_count = 0
    space_count = 0
    
    unknown_count = 0
    try:
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            words = file_contents.split()
            wordcount = len(words)
            print(f"Total number of words: {wordcount}")

            lower_file_contents = file_contents.lower()
            lettercount = 0
            alpha_letters = []
            for char in lower_file_contents:
                if char.isalpha():
                    lettercount += 1
                    alpha_letters.append(char)
                    for letter in alpha_letters:
                        if letter == "a":
                            a_count += 1
                        if letter == "b":
                            b_count += 1
                        if letter == "c":
                            c_count += 1
                        if letter == "d":
                            d_count += 1
                        if letter == "e":
                            e_count += 1
                        if letter == "f":
                            f_count += 1
                        if letter == "g":
                            g_count += 1
                        if letter == "h":
                            h_count += 1
                        if letter == "i":
                            i_count += 1
                        if letter == "j":
                            j_count += 1
                        if letter == "k":
                            k_count += 1
                        if letter == "l":
                            l_count += 1
                        if letter == "m":
                            m_count += 1
                        if letter == "n":
                            n_count += 1
                        if letter == "o":
                            o_count += 1
                        if letter == "p":
                            p_count += 1
                        if letter == "q":
                            q_count += 1
                        if letter == "r":
                            r_count += 1
                        if letter == "s":
                            s_count += 1
                        if letter == "t":
                            t_count += 1
                        if letter == "u":
                            u_count += 1
                        if letter == "v":
                            v_count += 1
                        if letter == "w":
                            w_count += 1
                        if letter == "q":
                            x_count += 1
                        if letter == "y":
                            y_count += 1
                        if letter == "z":
                            z_count += 1
                        if letter == " ":
                            space_count += 1
                        else: 
                            pass

                print(f"Total number of letters: {lettercount}")
                print(f"A count: {a_count}")
                print(f"B count: {b_count}")
                print(f"C count: {c_count}")
                print(f"D count: {d_count}")
                print(f"E count: {e_count}")
                print(f"F count: {f_count}")
                print(f"G count: {g_count}")
                print(f"H count: {h_count}")
                print(f"I count: {i_count}")
                print(f"J count: {j_count}")
                print(f"K count: {k_count}")
                print(f"L count: {l_count}")
                print(f"M count: {m_count}")
                print(f"N count: {n_count}")
                print(f"O count: {o_count}")
                print(f"P count: {p_count}")
                print(f"Q count: {q_count}")
                print(f"R count: {r_count}")
                print(f"S count: {s_count}")
                print(f"T count: {t_count}")
                print(f"U count: {u_count}")
                print(f"V count: {v_count}")
                print(f"W count: {w_count}")
                print(f"X count: {x_count}")
                print(f"Y count: {y_count}")
                print(f"Z count: {z_count}")
                print(f"total unknown characters: {unknown_count}")

    except FileNotFoundError:
        print("The file 'books/frankenstein.txt' was not found. Please check the path and try again." )
    except Exception as e:
        print(f"An error occured: {e}")
        
main()
import numpy as np

def plaintext(language):
    text_input = input('Enter text: ')

    P = []

    for letter in text_input:
        if letter in language.c:
            P.append(language.c.index(letter))
        elif letter in language.s:
            P.append(language.s.index(letter))

    return np.array(P)
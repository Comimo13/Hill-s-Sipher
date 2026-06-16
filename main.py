"""This is Hill's Sipher based on NumPy. Currently I'm learning NumPy as well don't judge strictly"""

from database import Latin_Script
from database import Cyrillic_Script
from database import Japanese_Scripts
from database import Spanish_Script
from database import Korean_Hangul
from database import Bengali_Script
from database import Devanagari_Script
from database import Hebrew_Script
from database import Greek_Script
from database import Arabic_Script
from database import German_Script

import numpy as np

try:
    def main():
        mapping = {
            'Latin': Latin_Script,
            'Cyrillic': Cyrillic_Script,
            'Japanese': Japanese_Scripts,
            'Spanish': Spanish_Script,
            'Korean': Korean_Hangul,
            'Bengali': Bengali_Script,
            'Devanagari': Devanagari_Script,
            'Hebrew': Hebrew_Script,
            'Greek': Greek_Script,
            'Arabic': Arabic_Script,
            'German': German_Script
        }
        for num, lang in enumerate(mapping):
            print(num, lang)

        language_input = input('Enter language: ')
        text_input = input('')

        P = []

        language = mapping[language_input]

        for letter in text_input:
            if letter in language.c:
                P.append(language.c.index(letter))
            elif letter in language.s:
                P.append(language.s.index(letter))

        K = np.array(
            [[3, 3],
            [2, 5]])
        P = np.array(P)
        N = len(language.c)
        C = np.dot(P , K) % N
        text_output = ''

        for i in C:
            text_output += language.c[i]

        print(text_output)

    main()

except Exception as e:
    print('fatal error: ' , e)
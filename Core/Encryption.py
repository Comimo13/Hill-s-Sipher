""". There is main functions of Hill's Sipher"""

import numpy as np

from Core import cipher_key
from Core.language import choose_language
from Core.plaintext import plaintext
from Core.cipher_key import K

def main():
    language = choose_language()
    P = plaintext()

    if len(P) % 2 != 0:
        P.append(language.c.index('X'))

    P = np.array(P)

    if len(P) > len(K):
        P = P.reshape(-1, 2)

    N = len(language.c)
    C = np.dot(P, K) % N

    text_output = ''

    C = C.flatten()

    for i in C:
        text_output += language.c[i]

    print(text_output)
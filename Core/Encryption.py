"""Encryption. Siphering the text with Hill's Sipher"""

import numpy as np

from Core.language import choose_language
from Core.plaintext import plaintext
from Core.cipher_key import K
from Core.ciphertext import Ciphertext
from Core.modulusN import modulusN

def encrypt():
    language = choose_language()
    P = plaintext(language)
    N = modulusN(language)

    if len(P) % 2 != 0:
        P.append(language.c.index('X'))

    P = np.array(P)

    if len(P) > len(K):
        P = P.reshape(-1, 2)
    C = Ciphertext(P, K, N)

    text_output = ''

    C = C.flatten()

    for i in C:
        text_output += language.c[i]

    print(text_output)
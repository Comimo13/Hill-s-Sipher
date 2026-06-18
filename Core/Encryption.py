"""Encryption. Siphering the text with Hill's Sipher"""

import numpy as np

from Core.cipher_key import K
from Core.ciphertext import Ciphertext
from Core.language import choose_language
from Core.modulusN import modulusN
from Core.plaintext import plaintext


def encrypt():
    language = choose_language()
    P = plaintext(language)
    N = modulusN(language)

    block_size = K.shape[1]
    pad = 0
    while len(P) % block_size != 0:
        P = list(P)
        P.append(pad)

    P = np.array(P)
    P = P.reshape(-1, block_size)

    C = Ciphertext(P, K, N)

    text_output = ""

    for i in C.flatten():
        text_output += language.c[i]

    print(text_output)
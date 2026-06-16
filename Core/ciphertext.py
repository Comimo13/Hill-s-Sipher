import numpy as np

def Ciphertext(P, K, N):
    C = np.dot(P, K) % N
    return C



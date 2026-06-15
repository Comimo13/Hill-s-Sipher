import numpy as np

"""This is Hill's Sipher based on NumPy. Currently I learning NumPy as well don't judge strictly"""

text_input = input('')

c_eng = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ'
s_eng = 'abcdefghijklmnopqrstuvwyxz'

P = []

for letter in text_input:
    if letter in c_eng:
        P.append(c_eng.index(letter))
    elif letter in s_eng:
        P.append(s_eng.index(letter))


K = np.array(
    [[3, 3],
    [2, 5]])
P = np.array(P)
N = len(c_eng)

C = np.dot(P , K) % N

text_output = ''

for i in C:
    text_output += c_eng[i]

print(text_output)

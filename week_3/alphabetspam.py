"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Alphabet Spam

Link: https://open.kattis.com/contests/qkxmff/problems/alphabetspam

@author Leonard Hußke

@version 1.0, 08.11.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.07s

"""

input_str = input()

n_all_chars = len(input_str)
ws = 0
lcl = 0
ucl = 0
s = 0
test = []

for c in input_str:
    if c.isupper():
        ucl += 1

    if c.islower():
        lcl += 1

    if not c.isalnum() or c.isnumeric():
        if c == "_":
            ws += 1
        else:
            s += 1

print(ws / n_all_chars)
print(lcl / n_all_chars)
print(ucl / n_all_chars)
print((s) / n_all_chars)

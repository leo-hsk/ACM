"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Mirror Images

Link: https://open.kattis.com/contests/qkxmff/problems/mirror

@author Leonard Hußke

@version 1.0, 14.11.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.07s

"""

def reverse_img(rows):
    img = ""
    for r in range(rows):
        row = input()
        img += row

        if r != rows - 1:
            img += "\n"
    print(img[::-1])


n_test_cases = int(input())

for t in range(n_test_cases):
    print(f"Test {t + 1}")
    img_data = input().split()
    rows = int(img_data[0])

    reverse_img(rows)
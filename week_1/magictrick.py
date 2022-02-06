"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Magic Trick

Link: https://open.kattis.com/contests/kp9a7t/problems/magictrick

@author Leonard Hußke

@version 1.0, 30.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.06s

"""

word = input()

def double_char(word):
    for i, v in enumerate(word):
        for i2, v2 in enumerate(word):
            if i2 == i:
                break
            if v == v2:
                print(0)
                return
    print(1)
double_char(word)
"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: How Many Digits?

Link: https://open.kattis.com/contests/e7uxa8/problems/howmanydigits

@author Leonard Hußke

@version 1.0, 21.11.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.13s

"""

import math


def calc_digits(n):
    if (n < 0):
        return 0

    if (n <= 1):
        return 1
    x = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) / 2.0))
    return math.floor(x) + 1


while True:
    try:
        n = int(input())
        print(calc_digits(n))

    except EOFError:
        break
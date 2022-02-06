"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Perfect Pth Powers

Link: https://open.kattis.com/problems/perfectpowers

@author Leonard Hußke

@version 1.0, 20.11.2021

Method : Ad-Hoc

Status : Not Accepted -  Run Time Error

Explanation : One of two test cases is accepted.

Runtime: 0.07s

"""

import math


def perfect_pth_power(n):
    if n == 1:
        return 1
    counter = int(math.log(n) // math.log(2) + 100)
    p = 1
    for i in range(counter):
        if (i <= 1):
            continue
        exponent = (int)(math.log(n) / math.log(i))
        for j in [exponent - 1, exponent, exponent + 1]:
            if i ** j == n:
                p = j
                return p
    return p


while True:
    n = int(input())

    if n == 0:
        break
    print(perfect_pth_power(n))
"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Billiard

Link: https://open.kattis.com/problems/billiard

@author Leonard Hußke

@version 1.0, 24.01.2022

Method : Ad-Hoc

Status : Accepted

Runtime: 0.06s

"""

import math


def area(x):
    return x * x


def format(x):
    return f"{round(x, 2):.2f}"


while True:
    a, b, s, m, n = [int(x) for x in input().split()]

    if a == b == s == m == n == 0:
        break

    # total horizontal distance
    horizontal = a * m
    # total vertical distance
    vertical = b * n

    # pythagoras
    total = math.sqrt(area(vertical) + area(horizontal))
    angle = math.degrees(math.atan(vertical / horizontal))
    # total distance / time
    velocity = total / s

    print(format(angle), format(velocity))

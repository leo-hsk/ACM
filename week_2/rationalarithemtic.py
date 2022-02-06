"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Rational Arithmetic

Link: https://open.kattis.com/contests/guve43/problems/rationalarithmetic

@author Leonard Hußke

@version 1.0, 08.11.2021

Method : Ad-Hoc

Status : Not Accepted

Explanation : Same logic as rationalarithmetic.java but it was not accepted.
              It could be that the virtual machine of Kattis handles the Integers different,
              because in pyhton they are usually unbound. Locally everything works fine.

Runtime: 0.89s

"""

import math


def addition(x1, x2, y1, y2):
    denumerator = x2 * y2
    numerator_x = x1 * y2
    numerator_y = x2 * y1
    numerator = numerator_x + numerator_y
    gcd = math.gcd(numerator, denumerator)
    return check_for_negative([int(numerator / gcd), int(denumerator / gcd)])


def substitution(x1, x2, y1, y2):
    denumerator = x2 * y2
    numerator_x = x1 * y2
    numerator_y = x2 * y1
    numerator = numerator_x - numerator_y
    gcd = math.gcd(numerator, denumerator)
    return check_for_negative([int(numerator / gcd), int(denumerator / gcd)])


def multiplication(x1, x2, y1, y2):
    numerator = x1 * y1
    denumerator = x2 * y2
    gcd = math.gcd(numerator, denumerator)
    return check_for_negative([int(numerator / gcd), int(denumerator / gcd)])


def division(x1, x2, y1, y2):
    numerator = x1 * y2
    denumerator = x2 * y1
    gcd = math.gcd(numerator, denumerator)
    return check_for_negative([int(numerator / gcd), int(denumerator / gcd)])


def check_for_negative(tup):
    if tup[1] < 0:
        tup[0] = tup[0] * -1
        tup[1] = tup[1] * -1
    return tup


def format_res(tup):
    if tup[0] == 0:
        print(0)
    else:
        print(f"{tup[0]} / {tup[1]}")


counter = int(input())
for i in range(counter):
    input_arr = input().split()
    x1, x2, op, y1, y2 = input_arr
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    res = []

    if op == "+":
        res = addition(x1, x2, y1, y2)
    elif op == "-":
        res = substitution(x1, x2, y1, y2)
    elif op == "*":
        res = multiplication(x1, x2, y1, y2)
    elif op == "/":
        res = division(x1, x2, y1, y2)

    format_res(res)
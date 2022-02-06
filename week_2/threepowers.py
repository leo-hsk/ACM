"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Three Powers

Link: https://open.kattis.com/contests/guve43/problems/threepowers

@author Leonard Hußke

@version 1.0, 29.11.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.13s

"""

from math import log


def PowTwoGen():
    n = 0
    while True:
        yield 3 ** n
        n += 1


def get_set(n:int):
    if n <= 0 :
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [3]
    power = PowTwoGen()
    l = int(log(n, 2))
    se = 2**l
    starter = 3**l

    m = n-se
    comb = get_set(m)
    comb.append(starter)
    comb.sort()
    return comb



def format(arr):
    if len(arr)==0:
        print("{ }")
        return
    print("{ ", end="")
    for i, x in enumerate(arr):
        print(x, end="")
        if (i+1)<len(arr):
            print(", ", end="")
    print(" }")


while True:
    n = int(input())
    if n==0:
        break
    n = n-1
    format(get_set(n))
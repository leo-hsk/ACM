"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Goldbach's Conjecture

Link: https://open.kattis.com/contests/guve43/problems/goldbach2

@author Leonard Hußke

@version 1.0, 01.11.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.89s

"""

import math

primes = [2, 3]
p_paires = {}


def prime(n):
    for num in range(2, int(math.sqrt(n) + 1)):
        if (n % num) == 0:
            return False
    return True


def all_primes(n):
    for i in range(3, n):
        if prime(i):
            primes.append(i)


def calc_n(n):
    all_primes(n)
    for p in primes:
        if p > n / 2:
            return
        for p2 in primes:
            if p + p2 == n:
                p_paires[p] = p2


def format_res(n):
    calc_n(n)
    print(f'{n} has {len(p_paires)} representation(s)')
    for key, value in p_paires.items():
        print(f'{key}+{value}')
    print()


counter = int(input())

for i in range(counter):
    format_res(int(input()))
    primes = [2, 3]
    p_paires = {}
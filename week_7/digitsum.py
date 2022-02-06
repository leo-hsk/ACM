"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Digit Sum

Link: https://open.kattis.com/problems/digitsum

@author Leonard Hußke

@version 1.0, 12.12.2021

Method : Ad-Hoc

Status : Not Accepted

Explanation : Wrong Answer

Runtime: /

"""

def count_digit_sum(d, p):
    s = [0] * 10
    s[d] = 1
    for i in range(1, d):
        s[i] += int(10**p)
    for i in range(1, 10):
        s[i] += int(d*(p*10**(p-1)))
    return s


def calc(a):
    prev = 0
    s = 0
    for i in range(len(str(a))-1, -1, -1):
        d = int(str(a//(10**i))[-1])
        sc = count_digit_sum(d, i)
        for j in range(1, 10):
            s += sc[j] * j
        s += prev * d * (10**i)
        prev += d
    return s


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        print(calc(b))

    elif b == 0:
        print(calc(a))

    else:
        print(calc(b) - calc(a) + 10)

"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Exact Change

Link: https://open.kattis.com/contests/pe4egm/problems/exactchange2

@author Leonard Hußke

@version 1.0, 13.12.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.07s

"""

cases = int(input())

for _ in range(cases):
    target = int(input())
    n_bills = int(input())
    bills = [int(input()) for x in range(n_bills)]

    dp = [float("inf")] * 10001  # until index 10000

    dp[0] = 0
    for b in bills:
        for v in range(10000 - b, -1, -1):
            if dp[v] != float("inf"):
                dp[v + b] = min(dp[v + b], dp[v] + 1)

    for x in range(target, len(dp)):
        if dp[x] != float("inf"):
            print(x, dp[x])
            break
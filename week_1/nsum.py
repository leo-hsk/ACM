"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: N-sum

Link: https://open.kattis.com/problems/nsum

@author Leonard Hußke

@version 1.0, 25.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.05s

"""

counter = int(input())
numbers = input().split()
numbers = list(map(int, numbers))
print(sum(numbers))
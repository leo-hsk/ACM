"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Reverse

Link: https://open.kattis.com/problems/ofugsnuid

@author Leonard Hußke

@version 1.0, 25.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.18s

"""

counter = int(input())
numbers = []

for i in range(counter):
    numbers.append(int(input()))

reversed = numbers[::-1]

for x in reversed:
    print(x)
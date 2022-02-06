"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Pot

Link: https://open.kattis.com/problems/pot

@author Leonard Hußke

@version 1.0, 30.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.05s

"""

counter = int(input())
res = 0

for i in range(counter):
    number = input()
    poww = int(number[-1])
    num = int(number[:-1])
    res += pow(num, poww)
print(res)
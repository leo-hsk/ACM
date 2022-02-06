"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Quality-Adjusted Life-Year

Link: https://open.kattis.com/problems/qaly

@author Leonard Hußke

@version 1.0, 30.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.05s

"""

numbers = input().split()
periods = int(numbers[0])
acc = 0.0

for i in range(periods):
    data = input().split()
    acc += float(data[0]) * float(data[1])
print(acc)
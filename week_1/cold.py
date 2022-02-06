"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Cold-puter Science

Link: https://open.kattis.com/problems/cold

@author Leonard Hußke

@version 1.0, 25.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.05s

"""

count = int(input())
res = 0
degrees = input().split()

for i in range(count):
    if int(degrees[i]) < 0:
        res += 1
        
print(res)
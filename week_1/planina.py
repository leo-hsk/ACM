"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Planina

Link: https://open.kattis.com/problems/planina

@author Leonard Hußke

@version 1.0, 25.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.05s

"""

counter = int(input())
points = 0
squares_in_row = 0

for i in range(1, counter+1):
    squares_in_row = 2 ** i + 1

points = squares_in_row ** 2

print(points)
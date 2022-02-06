"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Triangle Area

Link: https://open.kattis.com/problems/triarea

@author Leonard Hußke

@version 1.0, 25.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.05s

"""

data = input().split()
height = float(data[0])
base = float(data[1])
area = (height * base) / 2.0

print(area)
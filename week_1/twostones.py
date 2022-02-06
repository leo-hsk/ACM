"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Take Two Stones

Link: https://open.kattis.com/problems/twostones

@author Leonard Hußke

@version 1.0, 25.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.05s

"""

number = int(input())
if number % 2 == 0:
    print("Bob")
else:
    print("Alice")
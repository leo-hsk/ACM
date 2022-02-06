"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Jumbo Javelin

Link: https://open.kattis.com/contests/kp9a7t/problems/jumbojavelin

@author Leonard Hußke

@version 1.0, 28.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.06s

"""

counter = int(input())
sum = 0

for i in range(counter):
    sum += int(input())
sum -= counter -1
print(sum)
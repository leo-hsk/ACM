"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Tarifa

Link: https://open.kattis.com/problems/tarifa

@author Leonard Hußke

@version 1.0, 25.10.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.05s

"""

inital_megabytes = int(input())
num_months = int(input())
available_megabytes = inital_megabytes

for i in range(num_months):
    available_megabytes -= int(input())
    available_megabytes += inital_megabytes

print(available_megabytes)
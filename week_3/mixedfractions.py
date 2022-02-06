"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Mixed Fractions

Link: https://open.kattis.com/contests/qkxmff/problems/mixedfractions

@author Leonard Hußke

@version 1.0, 14.11.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.08s

"""

while True:
    data = input()

    if data == "0 0":
        break

    nominator = int(data.split()[0])
    denominator = int(data.split()[1])
    mix = nominator // denominator
    dif = nominator % denominator

    print(f"{mix} {dif} / {denominator}")
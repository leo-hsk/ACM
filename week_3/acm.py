"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: ACM Contest Scoring

Link: https://open.kattis.com/contests/qkxmff/problems/acm

@author Leonard Hußke

@version 1.0, 14.11.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.06s

"""

lookup = {}
sum_solved = 0
sum_minutes = 0

while True:
    line = input()
    min = int(line.split()[0])

    if min == -1:
        break

    id = line.split()[1]
    solved = True if line.split()[2] == "right" else False

    if id not in lookup:
        lookup[id] = {"min": min, "solved": solved, "penalty_min": 0 if solved else 20}
    else:
        if not lookup.get(id)["solved"]:
            penalties = lookup.get(id)["penalty_min"]
            lookup[id] = {"min": min, "solved": solved, "penalty_min": penalties if solved else penalties + 20}

for id in lookup:
    if lookup.get(id)["solved"]:
        sum_solved += 1
        sum_minutes += lookup.get(id)["min"] + lookup.get(id)["penalty_min"]

print(sum_solved, sum_minutes)
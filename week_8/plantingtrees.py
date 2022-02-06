"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Planting Trees

Link: https://open.kattis.com/problems/plantingtrees

@author Leonard Hußke

@version 1.0, 29.12.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.08s

"""

num_trees = int(input())
trees = [int(x) for x in input().split()]

trees.sort(reverse=True)

count_days = trees[0] + 2
for i in range(0, num_trees):
    if trees[i] + i+2 > count_days:
        count_days = trees[i] + i+2

print(count_days)
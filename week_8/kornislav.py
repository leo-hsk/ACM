"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Kornislav

Link: https://open.kattis.com/contests/nytf6n/problems/kornislav

@author Leonard Hußke

@version 1.0, 13.12.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.05s

"""

nums = [int(x) for x in input().split()]
nums.sort()
max_area = nums[0] * nums[2]
print(max_area)
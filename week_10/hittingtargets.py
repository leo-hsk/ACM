"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Hitting the Targets

Link: https://open.kattis.com/problems/hittingtargets

@author Leonard Hußke

@version 1.0, 22.01.2022

Method : Ad-Hoc

Status : Accepted

Runtime: 0.06s

"""


def get_targets():
    for i in range(num_targets):
        data = input().split()

        if data[0] == "rectangle":
            rectangles.append([int(x) for x in data[1:]])
        else:
            circles.append([int(x) for x in data[1:]])


def calc_hits():
    for i in range(num_shots):
        hits = 0
        x, y = [int(x) for x in input().split()]

        for x1, y1, x2, y2 in rectangles:
            if x1 <= x <= x2 and y1 <= y <= y2:
                hits += 1

        for x_center, y_center, r in circles:
            # pythagoras
            if (x - x_center) ** 2 + (y - y_center) ** 2 <= r ** 2:
                hits += 1
        print(hits)


rectangles = []
circles = []

num_targets = int(input())
get_targets()
num_shots = int(input())
calc_hits()

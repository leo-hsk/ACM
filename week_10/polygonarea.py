"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Polygon Area

Link: https://open.kattis.com/problems/polygonarea

@author Leonard Hußke

@version 1.0, 24.01.2022

Method : Ad-Hoc

Status : Accepted

Runtime: 0.09s

"""


def calc_area_of_polygon(vertices):
    mult_x = 0
    mult_y = 0
    for i in range(len(vertices) - 1):
        mult_x += + (vertices[i][0] * vertices[i + 1][1])
        mult_y += (vertices[i][1] * vertices[i + 1][0])
    area = (mult_x - mult_y) / 2

    direction = "CCW" if area >= 0 else "CW"

    print(direction, round(area if area > 0 else area * -1, 1))


while True:
    vertices = []
    no_vertices = int(input())

    if no_vertices == 0:
        break

    for i in range(no_vertices):
        nums = [int(x) for x in input().split()]
        vertices.append(nums)
    vertices = vertices + vertices[0:1]

    calc_area_of_polygon(vertices)

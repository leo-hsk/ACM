"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Convex Polygon Area

Link: https://open.kattis.com/problems/convexpolygonarea

@author Leonard Hußke

@version 1.0, 17.01.2022

Method : Ad-Hoc

Status : Accepted

Runtime: 0.06s

"""


def create_list_of_tuples():
    nums = [int(x) for x in input().split()]
    # add first point again
    nums = nums[1:] + nums[1:3]
    points = [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]
    return points


def calc_area_of_polygon(points):
    mult_x = 0
    mult_y = 0
    for i in range(len(points) - 1):
        mult_x += (points[i][0] * points[i + 1][1])
        mult_y += (points[i][1] * points[i + 1][0])
    area = (mult_x - mult_y) / 2
    return area


test_cases = int(input())
for i in range(test_cases):
    points = create_list_of_tuples()
    print(calc_area_of_polygon(points))


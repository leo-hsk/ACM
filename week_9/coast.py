"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Coast Length

Link: https://open.kattis.com/problems/coast

@author Leonard Hußke

@version 1.0, 16.01.2022

Method : Ad-Hoc

Status : Accepted

Runtime: 0.33s

"""

from collections import deque

coast_map = []
WATER = "0"
DIRECTIONS = [[0, -1], [1, 0], [0, 1], [-1, 0]];


def build_coast_map():
    rows, cols = [int(x) for x in input().split()]

    # store coast_map with water around
    coast_map.append([WATER for _ in range(cols + 2)])

    for i in range(rows):
        coast_map.append([WATER] + list(input()) + [WATER])

    coast_map.append([WATER for _ in range(cols + 2)])


def count_coastline():
    # lookup table to store if part of map was already visited
    visited = [[0 for _ in range(len(coast_map[0]))] for _ in range(len(coast_map))]

    number_coast_lines = 0

    # bfs to go through all map parts
    queue = deque()
    # start on the top left
    queue.append((0, 0))
    while len(queue) > 0:
        row, column = queue.pop()
        if visited[row][column] == 0:
            visited[row][column] = 1
            # ignore land
            if coast_map[row][column] == WATER:
                for dir in DIRECTIONS:
                    # check if on map
                    if 0 <= row + dir[0] < len(coast_map) and 0 <= column + dir[1] < len(coast_map[0]):
                        # add next part of map to explore
                        if coast_map[row + dir[0]][column + dir[1]] == WATER:
                            queue.append((row + dir[0], column + dir[1]))
                        else:
                            number_coast_lines += 1

    return number_coast_lines


build_coast_map()
print(count_coastline())

"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Ants

Link: https://open.kattis.com/contests/pmwidt/problems/ants

@author Leonard Hußke

@version 1.0, 03.12.2021

Method : Ad-Hoc

Status : Accepted

Runtime: 0.47s

"""

# Number testcases not needed
t = int(input())

while True:
    try:
        minimum = 0
        ants = []

        # Read values
        it = 0
        l, n = [int(x) for x in input().split()]
        while it != n:
            tmp = [int(x) for x in input().split()]
            ants.extend(tmp)
            it = it + len(tmp)

        for ant in ants:
            # min(ant, l - ant) check which direction is shorter for the current ant
            # max(xxx, minimum) check if current ant needs the most time to fall off
            minimum = max(min(ant, l - ant), minimum)

        ants.sort()
        # First and last ant on the pole and left and right direction to walk => 4 possibilities
        maximum = max([ants[0], ants[n - 1], l - ants[0], l - ants[n - 1]])

        print(minimum, maximum)

    except EOFError:
        break
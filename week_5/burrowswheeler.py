"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Burrows-Wheeler

Link: https://open.kattis.com/contests/zr36jo/problems/burrowswheeler

@author Leonard Hußke

@version 1.0, 15.11.2021

Method : Ad-Hoc

Status : Not Accepted - Memory Limit Exceeded

Explanation : I am using array and these are hold in memory all the time. Maybe I could use
              a different data structure e.g. something like a queue or in python a generator
              instead of an iterator, which would lead to less memory usage.

Runtime: 0.13s

"""

while True:
    try:
        string = input()
        arr = []
        out = ""

        for i in range(len(string)):
            if len(arr) == 0:
                arr.append(string)
            else:
                arr.append(arr[i - 1][1:] + arr[-1][0])

        arr.sort()
        for x in arr:
            out += x[-1]
        print(out)

    except EOFError:
        break
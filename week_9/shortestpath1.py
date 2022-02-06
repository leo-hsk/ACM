"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Single source shortest path, non-negative weights

Link: https://open.kattis.com/problems/shortestpath1

@author Leonard Hußke

@version 1.0, 10.01.2022

Method : Ad-Hoc

Status : Not Accepted

Explanation : Time Limit Exceeded

Runtime: > 3.00 s

"""

def build_graph():
    graph[start] = {start: 0}
    for x in range(no_edges):
        data = input().split()
        node = data[0]
        to_node = data[1]
        weight = int(data[2])

        if node not in graph:
            graph[node] = {to_node: weight}
        else:
            graph[node].update({to_node: weight})

        if to_node not in graph:
            graph[to_node] = {to_node: float("inf")}


def dijkstra(graph, start, goal):
    if start not in graph or goal not in graph:
        print("Impossible")
        return

    if start == goal:
        print(0)
        return

    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph
    infinity = float("inf")
    path = []
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessor[child_node] = min_node
        unseen_nodes.pop(min_node)

    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print("Impossible")
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
            print(shortest_distance[goal])


while True:
    graph = {}
    conf = [int(x) for x in input().split()]

    if conf == [0, 0, 0, 0]:
        break

    no_nodes = conf[0]
    no_edges = conf[1]
    no_queries = conf[2]
    start = str(conf[3])

    build_graph()
    # print(graph)
    for i in range(no_queries):
        goal = input()
        dijkstra(graph.copy(), start, goal)

    print("")

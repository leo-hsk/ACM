"""Ausgewählte Probleme aus dem ACM Programming Contest  WS 2021

Problem: Torn To Pieces

Link: https://open.kattis.com/problems/torn2pieces

@author Leonard Hußke

@version 1.0, 10.01.2022

Method : Ad-Hoc

Status : Accepted

Runtime: 0.06s

"""


def build_graph():
    for x in range(no_nodes):
        data = input().split()
        child_nodes = {}
        for child in data[1:]:
            child_nodes[child] = 1
            if child not in graph:
                graph[child] = {data[0]: 1}
            else:
                graph[child].update({data[0]: 1})

        if data[0] in graph:
            graph[data[0]].update(child_nodes)
        else:
            graph[data[0]] = child_nodes
            for child in child_nodes:
                if child in graph:
                    graph[child].update({data[0]: 1})
                else:
                    graph[child]: {data[0]: 1}


def dijkstra(graph, start, goal):
    if start not in graph or goal not in graph:
        print("no route found")
        return

    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph
    infinity = float("inf")
    path = []

    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    # calc all
    while unseen_nodes:
        min_node = None
        # node with less cost
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

    # get path from start to goal node
    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print("no route found")
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        # print(str(shortest_distance[goal]))
        for i in path:
            print(i, end=" ")


graph = {}
no_nodes = int(input())
build_graph()
start_goal = input().split()
dijkstra(graph, start_goal[0], start_goal[1])



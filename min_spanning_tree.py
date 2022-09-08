import sys
import pandas as pd
import math
import numpy as np


import time
from helper import util
from scipy.spatial import distance_matrix


def algorithm():
    minimum_dis = np.zeros((num_nodes,), dtype=float)  # distance wth start node as minimum_dis[i]
    route = [[] for y in range(0, num_nodes)]
    prev_nodes = [[0 for x in range(0, num_nodes)] for y in range(0, num_nodes)]
    print("Prim's mst:")
    for start in range(0, num_nodes):
        prev_nodes[start] = prims(start, num_nodes, graph)

    for start, parent in enumerate(prev_nodes):
        print("\nStartnode:" + str(start))
        print()
        route[start].append(start)
        i = 1
        while i < num_nodes:
            list = []
            for node, parent_node in enumerate(parent):
                if util.in_travel_route(parent_node, route[start]) and not util.in_travel_route(node, route[start]):
                    list.append(node)
                    i = i + 1
            for l in list:
                route[start].append(l)

        # to get distance
        prev_node = start
        cur_node = -1
        for i in range(1, num_nodes):
            cur_node = route[start][i]
            if graph[prev_node][cur_node] <= 0:
                minimum_dis[start] = float('inf')
            else:
                minimum_dis[start] = minimum_dis[start] + graph[prev_node][cur_node]
            print("from " + str(prev_node) + " to " + str(cur_node) +" distance: " + str(graph[prev_node][cur_node]))
            prev_node = cur_node

        if graph[cur_node][start] <= 0:
            minimum_dis[start] = float('inf')
        else:
            minimum_dis[start] = minimum_dis[start] + graph[cur_node][start]

    print("2 Approximation distance and path: ")
    [shortest_minimum_dis, shortest_route] = util.find_best_route(num_nodes, route, minimum_dis)

    return shortest_minimum_dis, shortest_route


def prims(start, num_nodes, graph):
    key = [float('inf') for x in range(0, num_nodes)]
    prev_node = [-1 for x in range(0, num_nodes)]
    unvisited = np.ones((num_nodes,), dtype=int)  
    key[start] = 0
    iteration = 1
    while util.check_unvisited_node(unvisited) and iteration < num_nodes:

        min_key_val = sys.maxsize
        min_node = num_nodes
        for i, key_val in enumerate(key):
            if unvisited[i] == 1 and key_val < min_key_val:
                min_key_val = key_val
                min_node = i

        unvisited[min_node] = 0

        # Updating nearby vertices
        for node, val in enumerate(key):
            if key[node] > graph[min_node][node] > 0 and unvisited[node] == 1:
                key[node] = graph[start][node]
                prev_node[node] = min_node

        iteration = iteration + 1



    return prev_node

if __name__ == '__main__':
    DF = pd.read_csv("C:/Users/NANI/OneDrive/Desktop/Algo project/Datasets/dj38 (1).csv")
    num_nodes1 = []
    tim1 = []
    for p in range(38,39):
        
        DF1 = DF[0:p]
        mat = pd.DataFrame(distance_matrix(DF1.values, DF1.values),index=DF1.index, columns=DF1.index)
        mat1 = mat.values.tolist()
        print(mat1)
        num_nodes = p
        print(p)
        graph = mat1
        start = time.time()
        algorithm()
        tottime = time.time() - start
        num_nodes1.append(p)
        tim1.append(tottime)

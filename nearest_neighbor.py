
import time
import pandas as pd
import numpy as np
from helper import util
import math
from scipy.spatial import distance_matrix

def algo():
    minimum_dis = np.zeros((num_nodes,), dtype=float)  # distance wth start node as minimum_dis[i]
    route = [[0 for i in range(0, num_nodes)] for j in range(0, num_nodes)]

    for start in range(0, num_nodes):
        unexplored = np.ones((num_nodes,), dtype=int)  #  nodes are unexplored
        unexplored[start] = 0
        route[start][0] = start  # the route starts with start

        node = start
        iteration = 1
        while util.check_unvisited_node(unexplored) and iteration < num_nodes:
            # Step 2
            nearby_arc = float('inf')
            nearby_node = num_nodes

            for node2 in range(0, num_nodes):
                if unexplored[node2] == 1 and 0 < graph[node][node2] < nearby_arc:
                    nearby_arc = graph[node][node2]
                    nearby_node = node2

            if nearby_node >= num_nodes:
                minimum_dis[start] = float('inf')
                break

            node = nearby_node
            unexplored[node] = 0
            minimum_dis[start] = minimum_dis[start] + nearby_arc
            # print(minimum_dis[start])
            route[start][iteration] = node
            iteration = iteration + 1

        if not math.isinf(minimum_dis[start]):
            last = route[start][num_nodes-1]
            if graph[last][start] > 0:
                minimum_dis[start] = minimum_dis[start] + graph[last][start]
            else:
                minimum_dis[start] = float('inf')
        print("min distance is: " + str(minimum_dis[start]))
        print(route[start])
        print()

    print("Nearest Neighbour distance and route:")
    [shortest_minimum_dis, shortest_route] = util.find_best_route(num_nodes, route, minimum_dis)

    return shortest_minimum_dis, shortest_route


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
        algo()
        tottime = time.time() - start
        num_nodes1.append(p)
        tim1.append(tottime)
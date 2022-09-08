
import tsplib95
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
problem = tsplib95.load('C:/Users/NANI/OneDrive/Desktop/Algo project/dj38.tsp') 
G = problem.get_graph() 
position = G.nodes(data="coord")

DF2 = pd.read_csv("C:/Users/NANI/Downloads/dj38.csv")
path = list(DF2['S.no'])

#Graph with normal city path
nx.draw_networkx_nodes(G, position)
nx.draw_networkx_labels(G, position)
nx.draw_networkx_edges(G, position, edgelist=list(zip(path, path[1:])))
plt.title('Cities of Djibouti')

#Greedy algorithm graph  7838.010502383545 in 0.09 seconds
path1 = [10, 11, 15, 16, 17, 18, 8, 7, 6, 5, 4, 2, 3, 1, 0, 9, 13, 20, 28, 29, 31, 34, 36, 37, 32, 33, 35, 30, 26, 27, 23, 21, 19, 22, 24, 25, 14, 12, 10]
path1 = [x+1 for x in path1]
nx.draw_networkx_nodes(G, position)
nx.draw_networkx_labels(G, position)
nx.draw_networkx_edges(G, position, edgelist=list(zip(path1, path1[1:])))
plt.title('Greedy Path')
#2-Opt path 1479.12 in 5.15 seconds
path2 = [32, 33, 35, 30, 26, 27, 23, 21, 19, 14, 12, 8, 11, 10, 16, 18, 17, 15, 7, 6, 5, 4, 2, 3, 1, 0, 9, 20, 13, 22, 24, 25, 29, 28, 31, 34, 36, 37,32]
path2 = [x+1 for x in path2]
nx.draw_networkx_nodes(G, position)
nx.draw_networkx_labels(G, position)
nx.draw_networkx_edges(G, position, edgelist=list(zip(path2, path2[1:])))
plt.title('Christofide path')

#Nearest neighbour path  6771.476577443569
path3 =[18, 17, 16, 15, 11, 10, 8, 7, 6, 5, 4, 2, 3, 1, 0, 9, 13, 20, 28, 29, 31, 34, 36, 37, 32, 33, 35, 30, 26, 27, 23, 21, 19, 22, 24, 25, 14, 12, 18]
path3 = [x+1 for x in path3]
nx.draw_networkx_nodes(G, position)
nx.draw_networkx_labels(G, position)
nx.draw_networkx_edges(G, position, edgelist=list(zip(path3, path3[1:])))
plt.title('Nearest neighbour Path')

#Minimum spanning tree algorithm Prim's heuristic  15369.215170276966

path4 = [37, 36, 32, 34, 31, 33, 35, 30, 27, 26, 29, 25, 23, 24, 21, 22, 28, 19, 18, 17, 16, 15, 14, 12, 11, 10, 8, 7, 6, 5, 13, 4, 20, 3, 2, 9, 1, 0, 37]
path4 = [x+1 for x in path4]
nx.draw_networkx_nodes(G, position)
nx.draw_networkx_labels(G, position)
nx.draw_networkx_edges(G, position, edgelist=list(zip(path4, path4[1:])))
plt.title('2-Approximation path')

#Genetic_TSP algorithm 9118.846 
path5 = [37, 36, 32, 34, 31, 33, 35, 30, 27, 26, 29, 25, 23, 24, 21, 22, 28, 19, 18, 17, 16, 15, 14, 12, 11, 10, 8, 7, 6, 5, 13, 4, 20, 3, 2, 9, 1, 0, 37]
path5 = [x+1 for x in path5]
nx.draw_networkx_nodes(G, position)
nx.draw_networkx_labels(G, position)
nx.draw_networkx_edges(G, position, edgelist=list(zip(path5, path5[1:])))
plt.title('Genetic Path')

#3/2 algorithm 9118.846
path6 = [14, 12, 6, 4, 5, 2, 3, 13, 9, 0, 1, 23, 15, 11, 16, 17, 18, 10, 29, 27, 31, 34, 26, 36, 32, 33, 30, 35, 37, 28, 21, 25, 24, 8, 7, 22, 20, 19, 14]
path6 = [x+1 for x in path6]
nx.draw_networkx_nodes(G, position)
nx.draw_networkx_labels(G, position)
nx.draw_networkx_edges(G, position, edgelist=list(zip(path6, path6[1:])))
plt.title('Christofide path')

#Experiment
path5 = [20, 28, 31, 29, 25, 23, 27, 35, 30, 26, 18, 17, 21, 14, 12, 15, 16,10, 11, 8, 7, 6, 5, 4, 2, 3, 1, 19, 22, 24, 32, 33, 38, 37, 36, 34, 13, 9, 20]
#path5 = [x+1 for x in path5]
nx.draw_networkx_nodes(G, position)
nx.draw_networkx_labels(G, position)
nx.draw_networkx_edges(G, position, edgelist=list(zip(path5, path5[1:])))
plt.title('Genetic Path')


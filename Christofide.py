#!/usr/bin/env python
# coding: utf-8

# In[1]:


def t_s_p(data):
    
    G = graph_build(data)
    print("Graph: ", G)

   
    M_S_T = m_s_t(G)
    print("Minimum Spanning Tree: ", M_S_T)

  
    node_odd = node_odd_find(M_S_T)
    print("Odd node in Minimum Spanning Tree: ", node_odd)

   
    matching_min_weight(M_S_T, G, node_odd)
    print("Minimum weight matching: ", M_S_T)

 
    eulerian_circuit = euler_circuit(M_S_T, G)

    print("Eulerian circuit: ", eulerian_circuit)

    curr = eulerian_circuit[0]
    path = [curr]
    visit = [False] * len(eulerian_circuit)
    visit[eulerian_circuit[0]] = True
    length = 0

    for v in eulerian_circuit:
        if not visit[v]:
            path.append(v)
            visit[v] = True

            length += G[curr][v]
            curr = v

    length +=G[curr][eulerian_circuit[0]]
    path.append(eulerian_circuit[0])

    print(" Path: ", path)
    print("length of the path: ", length)

    return length, path


def dist(a1, b1, a2, b2):
    return ((a1 - a2) ** 2 + (b1 - b2) ** 2) ** (1.0 / 2.0)


def graph_build(data):
    G = {}
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                if i not in G:
                    G[i] = {}

                G[i][j] = dist(data[i][0], data[i][1], data[j][0],
                                                        data[j][1])

    return G


class Find_Union:
    def __init__(self):
        self.costs = {}
        self.prev_node = {}

    def __getitem__(self, k):
        if k not in self.prev_node:
            self.prev_node[k] = k
            self.costs[k] = 1
            return k

        p = [k]
        root = self.prev_node[k]
        while root != p[-1]:
            p.append(root)
            root = self.prev_node[root]

        for i in p:
            self.prev_node[i] = root
        return root

    def __iter__(self):
        return iter(self.prev_node)

    def union(self, *objects):
        base = [self[x] for x in objects]
        max_weight = max([(self.costs[r], r) for r in base])[1]
        for r in base:
            if r != max_weight:
                self.costs[max_weight] += self.costs[r]
                self.prev_node[r] = max_weight


def m_s_t(G):
    t = []
    tree_sub = Find_Union()
    for W, i, j in sorted((G[i][j], i, j) for i in G for j in G[i]):
        if tree_sub[i] != tree_sub[j]:
            t.append((i, j, W))
            tree_sub.union(i, j)

    return t


def node_odd_find(MST):
    g_temp = {}
    nodes = []
    for edg in MST:
        if edg[0] not in g_temp:
            g_temp[edg[0]] = 0

        if edg[1] not in g_temp:
            g_temp[edg[1]] = 0

        g_temp[edg[0]] += 1
        g_temp[edg[1]] += 1

    for node in g_temp:
        if g_temp[node] % 2 == 1:
            nodes.append(node)

    return nodes


def matching_min_weight(MST, G, odd_node):
    import random
    random.shuffle(odd_node)

    while odd_node:
        b = odd_node.pop()
        lengt = float("inf")
        a = 1
        nearest = 0
        for a in odd_node:
            if b != a and G[b][a] < lengt:
                lengt = G[b][a]
                nearest = a

        MST.append((b, nearest, lengt))
        odd_node.remove(nearest)


def euler_circuit(MST_Matched, G):
   
    neighb = {}
    for i in MST_Matched:
        if i[0] not in neighb:
            neighb[i[0]] = []

        if i[1] not in neighb:
            neighb[i[1]] = []

        neighb[i[0]].append(i[1])
        neighb[i[1]].append(i[0])

   
    initial_vertex = MST_Matched[0][0]
    E = [neighb[initial_vertex][0]]

    while len(MST_Matched) > 0:
        for i, j in enumerate(E):
            if len(neighb[j]) > 0:
                break

        while len(neighb[j]) > 0:
            w = neighb[j][0]

            edge_removal(MST_Matched, j, w)

            del neighb[j][(neighb[j].index(w))]
            del neighb[w][(neighb[w].index(j))]

            i += 1
            E.insert(i, w)

            j = w

    return E


def edge_removal(Match_MST, n1, n2):

    for i, j in enumerate(Match_MST):
        if (j[0] == n2 and j[1] == n1) or (j[0] == n1 and j[1] == n2):
            del Match_MST[i]

    return Match_MST


# In[2]:


import pandas as pd
from scipy.spatial import distance_matrix
DF = pd.read_csv(r"C:\Users\chand\Desktop\Algorithms\Project\Circle_20.csv")

mat = pd.DataFrame(distance_matrix(DF.values, DF.values),index=DF.index, columns=DF.index)

mat1 = mat.values.tolist()


# In[3]:



t_s_p(mat1)


# In[ ]:





# In[ ]:





# In[ ]:





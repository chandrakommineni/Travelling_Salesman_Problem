#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import pandas as pd
import numpy as np
import math
import pulp
import time
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from tkinter   import Tk, Canvas
from random import randint, shuffle, randrange
from numba import jit
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Brute Force Approach

# In[8]:


## Brute Force Algorithm
from itertools import permutations
from math import hypot

def brute_force_algorithm(nodes):
    min_len = len_cal(nodes, range(len(nodes)))
    min_tour = range(len(nodes))

    for i in permutations(range(len(nodes))):
        lent = len_calc(nodes, i)
        if lent < min_len:
            min_len = lent
            min_tour = i

    return min_tour, min_len

def dist(n1, n2):
    x_1 = n2[0] - n1[0]
    x_2 = n2[1] - n1[1]

    return x_1**2 + x_2**2

def len_calc(nodes, tour):
    lent = 0
    for i in range(len(tour)):
        lent += dist(nodes[tour[i-1]], nodes[tour[i]])
    return lent


# In[9]:


file = open("C:/Users/vinee/OneDrive/Desktop/CS5800 Algos/Project/travelingSalesman-master/datasets/tsp0010.txt", 'r').read().splitlines()
no_nodes = file.pop(0)
nodes = np.array([tuple(map(float,coord.split())) for coord in file ])

#calculating path
strt_time = time.time()
tour, min_dist = brute_force_algorithm(nodes)
print(tour)

total_time = time.time() - strt_time
print( "Length of the tour is %s & time taken is %s seconds" % (round(math.sqrt(min_dist),2), round(total_time, 2) ) )


# ## Greedy Approach
# 

# In[13]:


from typing import DefaultDict

Max_value = 9999999999

def greedy_approach(mat):
    for i in range(15):
        val_sum = 0
        ctr = 0
        y = 0
        x = 0
        val_min = Max_value
        tour_vistd = DefaultDict(int)

        tour_vistd[0] = 1
        tour = [0] * len(mat)

        while x < len(mat) and y < len(mat[x]):

            if ctr >= len(mat[x]) - 1:
                break
                
            if y != x and (tour_vistd[y] == 0):
                if mat[x][y] < val_min:
                    val_min = mat[x][y]
                    tour[ctr] = y + 1

            y += 1
            
            if y == len(mat[x]):
                val_sum += val_min
                val_min = Max_value
                tour_vistd[tour[ctr] - 1] = 1
                y = 0
                x = tour[ctr] - 1
                ctr += 1

        x = tour[ctr - 1] - 1

        for j in range(len(mat)):

            if (x != j) and mat[x][j] < val_min:
                val_min = mat[x][j]
                tour[ctr] = j + 1

        val_sum += val_min

    print("Minimum Cost is :", val_sum)

    
### Main Code
if __name__ == "__main__":
 
    data = pd.read_csv("C:/Users/vinee/OneDrive/Desktop/CS5800 Algos/Project/travelingSalesman-master/datasets/dj38.csv")
    mat = pd.DataFrame(distance_matrix(data.values, data.values),index=data.index, columns=data.index)

    mat1 = mat.values.tolist()
    
    strt_time = time.time()
    greedy_approach(mat1)
    total_time = time.time() - strt_time
    
    print("time is ", total_time)





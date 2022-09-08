#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy
import math
import random
import matplotlib.pyplot as plt 


# In[2]:


import pandas as pd
from scipy.spatial import distance_matrix
DF = pd.read_csv(r"C:\Users\chand\Desktop\Algorithms\Project\dj38.csv")

mat = pd.DataFrame(distance_matrix(DF.values, DF.values),index=DF.index, columns=DF.index)

mat1 = mat.values.tolist()


# In[3]:


n_population = 20
n_cities = len(mat1[0])
tour_size = n_cities+1
population = []
tour_matrix = [[0 for i in range(tour_size)] for j in range(tour_size)]
first_parents = None
second_parents = None
distances = [0 for i in range(n_population)]
path_cost = []


# In[4]:


def population_generation():
    for _ in range(n_population):
        path = []
        for _ in range(1, n_cities + 1):
            random_city = random.randint(1,n_cities)
            while(duplicates(path, random_city)):
                random_city = random.randint(1,n_cities)
            path.append(random_city)
        population.append(path)

    
def duplicates(path, random_city):
    for city in path:
        if city == random_city:
            return True    
    return False


# In[5]:


def mutation(matrix):
    for i in range(len(matrix)):
        for _ in range(len(matrix[i])):
            ranNum = random.randint(1, 100)
            if ranNum >= 1 and ranNum <= 5:
                rand_city1 = random.randint(0,n_cities-1)
                rand_city2 = random.randint(0,n_cities-1)
                temp = matrix[i][rand_city1]
                matrix[i][rand_city1] = matrix[i][rand_city2]
                matrix[i][rand_city2] = temp


# In[6]:


def generate_tour_matrix():
    global tour_matrix
    tour_matrix = copy.deepcopy(population)
    for paths in tour_matrix:
        first_city = paths[0]
        paths.append(first_city)


# In[7]:


def fitness_function():
    global distances
    distances = [0 for _ in range(len(population))]
    for i in range(len(population)):
        for j in range(len(population[i])):
            firstPos = n_cities-1 if tour_matrix[i][j] == n_cities else tour_matrix[i][j]
            secondPos = n_cities-1 if tour_matrix[i][j+1] == n_cities else  tour_matrix[i][j+1]
            distances[i] += round(mat1[firstPos][secondPos], 4)
    dict_dist = {i: distances[i] for i in range(0, len(distances))}
    distances = copy.deepcopy(dict_dist)
    return sorted(distances.items(), key=lambda kv: kv[1])
    


# In[8]:


def rouletteFunction(sorted_x):
    global parentsOne
    global parentsTwo
    arr = []
    rouletteArr = []
    for i in range(10):
        arr.append(sorted_x[i][0])
    for j in range(len(arr)):
        for _ in range(10 - j):
            rouletteArr.append(arr[j])
    parentsOne = createParents(rouletteArr)
    parentsTwo = createParents(rouletteArr)


def createParents(rouletteArr):
    parentArr = []
    for _ in range(5):
        parentArr.append(rouletteArr[random.randint(0, 54)])
    return parentArr


# In[9]:



def is_duplicate(auxArray, usedIndexes):
    for i in range(len(auxArray)):
        for j in range(i, len(auxArray)):
            if i != j and auxArray[i] == auxArray[j]:
                if i in usedIndexes:
                    return j
                else:
                    return i
    return -1


# In[10]:



def perform_iteration(sorted_x):
    global population
    
    children = []

    for i in range(5):
        p_One_Aux = parentsOne[i]
        p_Two_Aux = parentsTwo[i]
        used_values = []

        random_Index = random.randint(0, n_population - 1)

        used_values.append(random_Index)

        first_child = copy.deepcopy(population[p_One_Aux])
        second_child = copy.deepcopy(population[p_Two_Aux])

        first_value = first_child[random_Index]
        second_value = second_child[random_Index]

        first_child[random_Index] = second_value
        second_child[random_Index] = first_value

        while(is_duplicate(first_child, used_values) != -1):
            newIndex = is_duplicate(first_child, used_values)
            used_values.append(newIndex)

            first_value = first_child[newIndex]
            second_value = second_child[newIndex]

            first_child[newIndex] = second_value
            second_child[newIndex] = first_value

        
        children.append(first_child)
        children.append(second_child)

    # Mutate the children array
    mutation(children)

    # Make a temp copy of the population before changing it
    temp_copy = copy.deepcopy(population)

    for i in range(10):
        population[i] = copy.deepcopy(temp_copy[sorted_x[i][0]])

    # Adjust the population
    for j in range(10, n_population):
        population[j] = copy.deepcopy(children[j - 10])


# In[11]:


def main():
    
    population_generation()
    generate_tour_matrix()
    global sorted_x

    
    for _ in range(5000):
        sorted_x = fitness_function()
        rouletteFunction(sorted_x)
        perform_iteration(sorted_x)
        generate_tour_matrix() 
        path_cost.append(sorted_x[0][1]) 
        
    # Generates the fitness values for the last population
    sorted_x = fitness_function()

    print('Total Population: %s' % (n_population))
    print('Mutation Probability: 5%')
    print('Number of cities: %s' % (n_cities))
    print('Optimal path cost: %s' % sorted_x[0][1])
    print('Best Route: %s' % population[0])

    # Show the path graph
    plt.plot(tour_matrix[0])
    plt.plot(tour_matrix[0], 'ro')
    plt.axis([0,tour_size , 0, tour_size])
    plt.show()

    # Show the cost graph
    plt.plot(path_cost)
    plt.show()

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





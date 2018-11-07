# -*- coding: utf-8 -*-

from random import randint

number_of_vertices = 500
filename = "graphs/graph" + str(number_of_vertices) + ".txt"
f = open(filename, "w+")

for i in range(number_of_vertices - 1):
    for j in range(i + 1, number_of_vertices):
        edge_weight = 0
        if (i < number_of_vertices/2 and j < number_of_vertices/2) or (i > 
           number_of_vertices/2 and j > number_of_vertices/2):
            edge_weight = randint(3, 6)
        else:
            edge_weight = randint(1, 3)
        f.write(str(i + 1) + " " + str(j + 1) + " " + str(edge_weight) + "\n")

    
f.close()


# -*- coding: utf-8 -*-

from graphLoading import load_graph
from partitioningFunctions import cut, external_cost, internal_cost
from random import randint
import operator
import networkx as nx
import time

def update_gains(G, V_new, labels, U, new_vertex, adjacency):
    #print("--- in the update_gains method ---")
    E = G.edges(data=True) 
    U_new = U
    
    neighbors = [(u, v) for u, v, d in E if u == new_vertex or
                 v == new_vertex]
    #print("neighbors of vertex" + str(new_vertex))
    #print(neighbors)
    #print("before the loop")
    for neighbor in neighbors:
        #print("in the loop")
        if neighbor[0] == new_vertex:
            vertex_to_add = neighbor[1]
        else:
            vertex_to_add = neighbor[0]
        #print("vertex to add: " + str(vertex_to_add))
        if vertex_to_add not in V_new:
            neighbor_gain = external_cost(G, labels, 
                          vertex_to_add, adjacency) - internal_cost(G, labels, vertex_to_add, adjacency)
        
            already_in_U = [(u, gain) for u, gain in U_new if u == vertex_to_add]
            if len(already_in_U) > 0:
                U_new.remove(already_in_U[0])
            
            U_new.append((vertex_to_add, neighbor_gain))
    
    U_new.sort(key=operator.itemgetter(1), reverse=True)
    return U_new

def greedy_graph_growing(G):
    V = G.nodes()    
    card = len(V)
    
    adjacency = nx.to_numpy_matrix(G, weight='weight')
    
    random_index = randint(0, card - 1)
    chosen_vertex = V[random_index]
    #print("chosen vertex: " + str(chosen_vertex))
    labels = []
    for vertex in V:
        labels.append(-1)
    
    # initializing new set of vertices and moving chosen vertex to the other part
    V_new = []
    V_new.append(chosen_vertex)
    labels[random_index] = 1
    U = []
        
    new_vertex = chosen_vertex
    while len(V_new) < int(card / 2):
        iteration_start = time.time()
        print("iteration: " + str(len(V_new)))
        U = update_gains(G, V_new, labels, U, new_vertex, adjacency)
        #print(U)
        new_vertex = U[0]
        #print("new_vertex: " + str(new_vertex))
        U.remove(new_vertex)
        new_vertex = new_vertex[0]
        V_new.append(new_vertex)
        new_index = V.index(new_vertex)
        labels[new_index] = 1
        iteration_end = time.time()
        print("iteration duration: " + str(iteration_end - iteration_start))
        
    return labels
 
if __name__ == "__main__":    
    file_name = 'graphs/graph500.txt'
    G = load_graph(file_name)
    adjacency = nx.to_numpy_matrix(G, weight='weight')
    start = time.time()
    print("start time: " + str(start))
    new_labels = greedy_graph_growing(G)
    end = time.time()
    print("time difference: " + str(end - start))
    print("vertices: ")
    print(G.nodes())
    print("labels: ")
    print(new_labels)
    print("cut computed: " + str(cut(G, new_labels, adjacency)))

    

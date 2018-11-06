# -*- coding: utf-8 -*-

import networkx as nx
from graphLoading import load_graph
from partitioningFunctions import cut, external_cost, internal_cost
from random import randint
import operator

def update_gains(G, V_new, labels, U, new_vertex):
    V = G.nodes()
    E = G.edges(data=True)    
    
    neighbors = [(u, v) for u, v, d in E if u == new_vertex or
                 v == new_vertex]
    for neighbor in neighbors:
        if neighbor[0] == new_vertex:
            vertex_to_add = neighbor[1]
        else:
            vertex_to_add = neighbor[0]
        print("vertex to add: " + str(vertex_to_add))
        if vertex_to_add not in V_new:
            neighbor_gain = external_cost(G, labels, 
                          vertex_to_add) - internal_cost(G, labels, vertex_to_add)
        
            already_in_U = [(u, gain) for u, gain in U if u == vertex_to_add]
            if len(already_in_U) > 0:
                U.remove(already_in_U[0])
            
            U.append((vertex_to_add, neighbor_gain))
    
    U.sort(key=operator.itemgetter(1), reverse=True)
    return U

def greedy_graph_growing(G):
    V = G.nodes()    
    E = G.edges(data=True)
    card = len(V)
    
    random_index = randint(0, card - 1)
    chosen_vertex = V[random_index]
    print("chosen vertex: " + str(chosen_vertex))
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
        U = update_gains(G, V_new, labels, U, new_vertex)
        print(U)
        new_vertex = U[0]
        U.remove(new_vertex)
        V_new.append(new_vertex[0])
        new_index = V.index(new_vertex[0])
        labels[new_index] = 1
        
    return labels
    
file_name = 'graphs/computeCutGraph.txt'
G = load_graph(file_name)
new_labels = greedy_graph_growing(G)
print("vertices: ")
print(G.nodes())
print("labels: ")
print(new_labels)
print("cut computed: " + str(cut(G, new_labels)))

    

# -*- coding: utf-8 -*-

import networkx as nx
from graphLoading import load_graph
from partitioningFunctions import cut, internal_cost, external_cost
import operator

def compute_IEcosts_differences(G, labels, locked=[]):
    V = G.nodes()
    D1 = []
    D2 = []
    for vertex in V:
        vertex_external_cost = external_cost(G, labels, vertex)
        vertex_internal_cost = internal_cost(G, labels, vertex)
        the_difference = vertex_external_cost - vertex_internal_cost
        
        vertex_index = V.index(vertex)
        vertex_label = labels[vertex_index]
        if vertex_label == 1:
            if vertex not in locked:
                D1.append((vertex, the_difference))
        else:
            if vertex not in locked:
                D2.append((vertex, the_difference))
    
    D1.sort(key=operator.itemgetter(1), reverse=True)
    D2.sort(key=operator.itemgetter(1), reverse=True)
    
    return (D1, D2)

def update_differences(G, labels, locked, D1_old, D2_old, v1, v2):
    V = G.nodes()
    E = G.edges(data=True)
    D1_new = []
    D2_new = []
    
    print("gains after changing vertices " + str(v1) + " and " + str(v2) + ": ")
    
    for vertex in V:
        if vertex not in locked:
            vertex_index = V.index(vertex)
            vertex_label = labels[vertex_index]
            vertex_difference = 0
            vertex_gain = []
            if vertex_label == 1:
                vertex_gain = [gain for v, gain in D1_old if v == vertex]
            else:
                vertex_gain = [gain for v, gain in D2_old if v == vertex]
            vertex_difference = vertex_gain[0]
            print("vertex_difference of vertex " + str(vertex) + ": "
                  + str(vertex_difference))
            
            edge_one = [(u, v, d) for u, v, d in E if (u == vertex and v == v1)
                            or (u == v1 and v == vertex)]
            print("edge one:")
            print(edge_one)
            edge_one_weight = 0
            if(len(edge_one) > 0):
                edge_one_weight = edge_one[0][2]['weight']
            print("edge_one_weight between " + str(v1) + " and " + str(vertex) + ": "
                  + str(edge_one_weight))           
            edge_two = [(u, v, d) for u, v, d in E if (u == vertex and v == v2)
                            or (u == v2 and v == vertex)]
            edge_two_weight = 0
            if(len(edge_two) > 0):
                edge_two_weight = edge_two[0][2]['weight']
            print("edge_two_weight between " + str(v2) + " and " + str(vertex) + ": "
                  + str(edge_two_weight))
                
            if vertex_label == 1:
                new_difference = vertex_difference + 2*edge_one_weight - 2 * edge_two_weight
                D1_new.append((vertex, new_difference))
            else:
                new_difference = vertex_difference - 2*edge_one_weight + 2*edge_two_weight
                D2_new.append((vertex, new_difference))
                
    return (D1_new, D2_new)
            
    

def find_max_gain(G, D1, D2):
    print("---------- find_max_gain function ----------")
    E = G.edges(data=True)
    max_gain = 0
    maxv1 = -1
    maxv2 = -1
    
    for difference1 in D1:
        vertex1 = difference1[0]
        first_difference = difference1[1]
        print("vertex1: " + str(vertex1))
        stop = 1
        for difference2 in D2:
            vertex2 = difference2[0]
            second_difference = difference2[1]
            iteration_gain = first_difference + second_difference
            print("vertex2: " + str(vertex2))
            print("iteration_gain without edge: " + str(iteration_gain))
            print()
            if maxv1 != -1 and iteration_gain <= max_gain:
                print("gain: " + str(max_gain))
                print()
                break
            edge = [(u, v, d) for u, v, d in E if (u == vertex1 and v == vertex2)
                        or (u == vertex2 and v == vertex1)]
            if(len(edge) > 0):
                to_add = edge[0][2]['weight']
                iteration_gain -= 2*to_add
            if (iteration_gain > max_gain) or (D1.index(difference1) == 0 and D2.index(difference2) == 0):
                max_gain = iteration_gain
                maxv1 = vertex1
                maxv2 = vertex2
            stop = 0
        if stop == 1:
            break
    
    return (maxv1, maxv2, max_gain)
        
def KernighanLin(G, labels):
    current_cut = cut(G, labels)
    V = G.nodes()
    card = len(V)
    
    while True:
        differences = compute_IEcosts_differences(G, labels)
        D1 = differences[0]
        D2 = differences[1]
        
        print("first part differences: ")
        print(D1)
        print("second part differences: ")
        print(D2)
        
        locked_vertices = []
        candidates_one = []
        candidates_two = []
        gains = []
        last_gain = 0
        
        for i in range(0, int(card/2)):
            to_change = find_max_gain(G, D1, D2)
            locked_vertices.append(to_change[0])
            locked_vertices.append(to_change[1])
            candidates_one.append(to_change[0])
            candidates_two.append(to_change[1])
            gains.append(to_change[2] + last_gain)
            last_gain = to_change[2] + last_gain
            
            new_differences = update_differences(G, labels, locked_vertices, D1, D2, 
                                                 to_change[0], to_change[1])
            
            D1 = new_differences[0]
            D2 = new_differences[1]
            
            print("D1 new: ")
            print(D1)
            print("D2 new: ")
            print(D2)
            
        print("candidates_one: ")
        print(candidates_one)
        print("candidates_two: ")
        print(candidates_two)
        print("gains: ")
        print(gains)
        
        max_gain = max(gains)
        gain_index = gains.index(max_gain)
        print("max gain found: " + str(max_gain))
        
        if max_gain > 0:
            gain_index = gains.index(max_gain)
            for i in range(0, gain_index + 1):
                v1_index = V.index(candidates_one[i])
                labels[v1_index] = labels[v1_index] * -1
                v2_index = V.index(candidates_two[i])
                labels[v2_index] = labels[v2_index] * -1
                current_cut = current_cut - max_gain
        else:
            return(labels, current_cut)
            
    
file_name = 'graphs/computeCutGraph.txt'
G = load_graph(file_name)
labels = [-1, 1, -1, -1, 1, 1]
result = KernighanLin(G, labels)
print("vertices: ")
print(G.nodes)
print("resulting labels: ")
print(result[0])
print("final cut: " + str(result[1]))


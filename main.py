# -*- coding: utf-8 -*-

import networkx as nx
from graphLoading import load_graph
from GGGP import greedy_graph_growing
from KernighanLin import KernighanLin
from partitioningFunctions import cut
from spectralPartitioning import spectral_partitioning
import time
from random import randint

if __name__ == "__main__":
    file_name = 'graphs/graph500.txt'
    G = load_graph(file_name)
    number_of_vertices = len(G.nodes())
    adjacency = nx.to_numpy_matrix(G, weight='weight')

    print("---------- starting spectral partitioning ----------")
    start = time.time()
    print("number of vertices: " + str(number_of_vertices))
    labels = spectral_partitioning(G)
    end = time.time()
    print("algorithm lasted: " + str(end - start))
    final_cut = cut(G, labels, adjacency)
    print("final cut: " + str(final_cut))
    print("-------------------")
    
    print()
    
    print("---------- starting K-L with spectral partitioning ----------")
    start = time.time()
    print("number of vertices: " + str(number_of_vertices))
    result = KernighanLin(G, labels)
    end = time.time()
    print("algorithm lasted: " + str(end - start))
    final_cut = result[1]
    print("final cut: " + str(final_cut))
    print("-------------------")
    
    print()
    
#    print("---------- starting GGGP ----------")
#    min_cut = 0
#    min_iter = 0
#    labels_for_KL = []
#    start = time.time()
#    for i in range(0, 4):
#        print("iteration: " + str(i + 1))
#        print("number of vertices: " + str(number_of_vertices))
#        labels = greedy_graph_growing(G)
#        final_cut = cut(G, labels, adjacency)
#        print("final cut: " + str(final_cut))
#        if i == 0 or final_cut < min_cut:
#            min_cut = final_cut
#            labels_for_KL = labels
#            min_iter = i + 1
#        print("--------------------")
#    end = time.time()
#    print("final min_cut: " + str(min_cut) + " found in iteration " + str(min_iter))
#    print("algorithm lasted: " + str(end - start))
#    print("--------------------------")
#    
#    print()
#    
#    print("---------- starting K-L with GGGP ----------")
#    start = time.time()
#    print("number of vertices: " + str(number_of_vertices))
#    result = KernighanLin(G, labels_for_KL)
#    end = time.time()
#    print("algorithm lasted: " + str(end - start))
#    final_cut = result[1]
#    print("final cut: " + str(final_cut))
#    print("-------------------")
#    
#    print()
    
#    print("initializing random labels")
#    labels = []
#    for label in range(0, 100):
#        labels.append(1) 
#    for i in range(0, int(number_of_vertices/2)):
#        print("i: " + str(i))
#        while True:
#            random_index = randint(0, number_of_vertices - 1)
#            #print("random index: " + str(random_index))
#            if labels[random_index] == 1:
#                labels[random_index] = -1
#                print("random_index: " + str(random_index))
#                break
#    print(labels)
#    
#    print()
#    
#    print("---------- starting K-L with random labels ----------")
#    start = time.time()
#    print("number of vertices: " + str(number_of_vertices))
#    result = KernighanLin(G, labels)
#    end = time.time()
#    print("algorithm lasted: " + str(end - start))
#    final_cut = result[1]
#    print("final cut: " + str(final_cut))
#    print("-------------------")
# -*- coding: utf-8 -

import networkx as nx
from graphLoading import load_graph
from HEM import HEM_coarsening
from GGGP import greedy_graph_growing
from KernighanLin import KernighanLin
import time

def multilevel(G):
    # list of graphs generated in the coarsening phase
    graphs_list = []
    graphs_list.append(G)
    G_new = G
    
    # coarsening
    while len(G_new.nodes()) > 500:
        G_new = HEM_coarsening(G_new)
        graphs_list.append(G_new)
        
if __name__ == "__main__":
    file_name = 'graphs/graph100.txt'
    G = load_graph(file_name)
    multilevel(G)
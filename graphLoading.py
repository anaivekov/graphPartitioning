# -*- coding: utf-8 -*-

import networkx as nx

def load_graph(file_name):
    G = nx.Graph()
    with open(file_name) as f:
        content = f.readlines()
        for line in content:
            line = line.rstrip()
            edge_info = line.split(' ')
            u = int(edge_info[0])
            v = int(edge_info[1])
            weight = int(edge_info[2])
            G.add_edge(u, v, {'weight' : weight, 'color': 'blue'})
    
    return G
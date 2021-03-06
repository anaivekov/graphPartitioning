# -*- coding: utf-8 -*-

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from graphLoading import load_graph
from partitioningFunctions import cut
import time
            
#for node in G.nodes(data=True):
#    node[1]['color'] = 'blue'
#node_colors = [d['color'] for n, d in G.nodes(data=True) ]
#edge_colors = [d['color'] for u, v, d in G.edges(data=True)]
#nx.draw_networkx_nodes(G, nx.circular_layout(G), node_size=1600, alpha=0.3, node_color=node_colors)
#nx.draw_networkx_edges(G, nx.circular_layout(G), width=2, alpha=0.1,edge_color=edge_colors)
#nx.draw_networkx_labels(G, nx.circular_layout(G), font_size=12, font_family='sans-serif')

#plt.show()
def spectral_partitioning(G):
    labels = []
    fiedler = nx.fiedler_vector(G, method = 'lanczos')
    median = np.median(fiedler)
    labels = []
    for i in range(len(fiedler)):
        if(fiedler[i] < median):
            labels.append(-1)
        else:
            labels.append(1)
    #print("labels:")
    #print(labels)
    
    return labels
#    i = 0
#    for node in G.nodes(data=True):
#        if labels[i] == -1:
#            node[1]['color'] = 'blue'
#        else:
#            node[1]['color'] = 'red'
#        i += 1
    
#node_colors = [d['color'] for n, d in G.nodes(data=True) ]
#edge_colors = [d['color'] for u, v, d in G.edges(data=True)]
#nx.draw_networkx_nodes(G, nx.circular_layout(G), node_size=1600, alpha=0.3, node_color=node_colors)
#nx.draw_networkx_edges(G, nx.circular_layout(G), width=2, alpha=0.1,edge_color=edge_colors)
#nx.draw_networkx_labels(G, nx.circular_layout(G), font_size=12, font_family='sans-serif')

#plt.show()

if __name__ == "__main__":
    file_name = 'graphs/graph100.txt'
    G = load_graph(file_name)
    start = time.time()
    print("start time: " + str(start))
    result = spectral_partitioning(G)
    print("labels: ")
    print(result)
    end = time.time()
    print("algorithm lasted: " + str(end - start))
    adjacency = nx.adjacency_matrix(G, weight='weight')
    print("final cut: " + str(cut(G, result, adjacency)))

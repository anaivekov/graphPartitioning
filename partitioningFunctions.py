# -*- coding: utf-8 -*-

from graphLoading import load_graph
import networkx as nx

# the method computes cut for a given graph and bipartition
def cut(G, P2, graph_adjacency_matrix):
    cut = 0
    V = G.nodes()
    E = G.edges(data=True)
    #print(E)
    #print("vertices: ")
    #print(V)
    vertex_index = 0
    for partition_label in P2:
        if partition_label == 1:
            #print("vertex index: " + str(vertex_index))
            vertex = V[vertex_index]
            #print("vertex: " + str(vertex))
            cut_vertex_index = 0
            for cut_partition_label in P2:
                if cut_partition_label == -1:
#                    cut_vertex = V[cut_vertex_index]
#                    #print("cut vertex index: " + str(cut_vertex_index))
#                    #print("cut_vertex: " + str(cut_vertex))
#                    cut_edges = [(u, v, d) for u, v, d in E if
#                                 (u == vertex and v == cut_vertex) or
#                                 (u == cut_vertex and v == vertex)]
#                    if(len(cut_edges) > 0):
#                        cut_to_add = cut_edges[0][2]['weight']
#                        #print("adding cut between " + str(vertex) + " and " +
#                              #str(cut_vertex) + ": " + str(cut_to_add))
                        cut += graph_adjacency_matrix[vertex_index, cut_vertex_index]
                cut_vertex_index += 1
        vertex_index += 1
        
    return cut

def internal_cost(G, labels, vertex, graph_adjacency_matrix):
    internal_cost = 0
    V = G.nodes()
    E = G.edges(data=True)
    vertex_index = V.index(vertex)
    #print("vertex: " + str(vertex))
    #print("vertex_index: " + str(vertex_index))
    vertex_label = labels[vertex_index]
    #print("vertex label: " + str(vertex_label))
    neighbor_index = 0
    for label in labels:
        if label == vertex_label:
            #neighbor = V[neighbor_index]
#            common_edge = [(u, v, d) for u, v, d in E if (
#                    u == vertex and v == neighbor) or( 
#                            u == neighbor and v == vertex)]
            #if(len(common_edge) > 0):
                #internal_cost_to_add = common_edge[0][2]['weight']
                #print("adding internal cost between " + str(vertex) +
                      #" and " + str(neighbor) + ": " + str(internal_cost_to_add))
            internal_cost += graph_adjacency_matrix[vertex_index, neighbor_index]
        neighbor_index += 1
    
    return internal_cost

def external_cost(G, labels, vertex, graph_adjacency_matrix):
    external_cost = 0
    V = G.nodes()
    E = G.edges(data=True)
    vertex_index = V.index(vertex)
    #print("vertex: " + str(vertex))
    #print("vertex_index: " + str(vertex_index))
    vertex_label = labels[vertex_index]
    #print("vertex label: " + str(vertex_label))
    neighbor_index = 0
    for label in labels:
        if label != vertex_label:
#            neighbor = V[neighbor_index]
#            common_edge = [(u, v, d) for u, v, d in E if (
#                    u == vertex and v == neighbor) or( 
#                            u == neighbor and v == vertex)]
#            if(len(common_edge) > 0):
#                external_cost_to_add = common_edge[0][2]['weight']
                #print("adding external cost between " + str(vertex) +
                      #" and " + str(neighbor) + ": " + str(external_cost_to_add))
            external_cost += graph_adjacency_matrix[vertex_index, neighbor_index]
        neighbor_index += 1
    
    return external_cost

#file_name = 'graphs/computeCutGraph.txt'
#G = load_graph(file_name)
#adjacency = nx.to_numpy_matrix(G, weight='weight')
#print(adjacency)
#print(adjacency[1, 3])
#print(adjacency.size)
#labels = [-1, 1, 1, -1, 1, -1]
#partition_cut = cut(G, labels, adjacency)
#print("final cut: " + str(partition_cut))
#V = G.nodes()
#vertex = V[4]
#internal_cost_one = internal_cost(G, labels, vertex, adjacency)
#print("final internal cost of the node " + str(vertex) + ": " +
#      str(internal_cost_one))
#external_cost_test = external_cost(G, labels, vertex, adjacency)
#print("final external cost of the node " + str(vertex) + ": " +
#      str(external_cost_test))
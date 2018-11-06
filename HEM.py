# -*- coding: utf-8 -*-

import networkx as nx
from graphLoading import load_graph
from random import randint

def HEM_coarsening(G):
    V = G.nodes()
    E_new = G.edges(data=True)
    #V_new = G.nodes(data=True)
    
    G_new = nx.Graph()
    
    print("checking edges")
    print(G.has_edge(1, 5))
    
    while len(V) > 0:
        # randomly select a vertex 
        random_index = randint(0, len(V) - 1)
        chosen_vertex = V[random_index]
        found = 0
        E_aux = []
        print(chosen_vertex)
        second_vertex = -1
        # select the edge of maximal weight
        weights = [d['weight'] for u, v, d in E_new if u == chosen_vertex or v == chosen_vertex]
        for w in weights:
            print(w)
        while True:
            max_weight = max(weights)
            print("max weight: " + str(max_weight))
            edges_to_coarsen = [(u, v, d) for u, v, d in E_new if (u == chosen_vertex or v == chosen_vertex)
                                               and d['weight'] == max_weight]
            for edge in edges_to_coarsen:
                if edge[0] in V and edge[1] in V:
                    edge_to_coarsen = edge
                    found = 1
                    break
            if found == 1:
                break
            
            weights.remove(max_weight)
        
        if(edge_to_coarsen[0] == chosen_vertex):
            second_vertex = edge_to_coarsen[1]
        else:
            second_vertex = edge_to_coarsen[0]
        edge_to_coarsen_vertices = (chosen_vertex, second_vertex)
        print("edge to coarsen: " + str(edge_to_coarsen))
        # add new vertex to the graf G_new
        G_new.add_node(chosen_vertex, {'parents': edge_to_coarsen_vertices})
        E_new.remove(edge_to_coarsen)
        print(G_new.nodes(data=True))
        # make neighbors lists for the first vertex
        edges_to_neighbors = [(u, v, d) for u, v, d in E_new if (u == chosen_vertex or v == chosen_vertex)]
        print("edges to neighbors:")
        print(edges_to_neighbors)
        for neighbor in edges_to_neighbors:
            if neighbor[0] == chosen_vertex:
                the_neighbor = neighbor[1]
            else:
                the_neighbor = neighbor[0]
                
            neighbors_second = [(u, v, d) for u, v, d in E_new if 
                                (u == the_neighbor and v == second_vertex) or
                                (u == second_vertex and v == the_neighbor)]
            print("neighbors second:")
            print(neighbors_second)
            if(len(neighbors_second) > 0):              # means the vertices have common neighbor
                new_edge_weight = neighbor[2]['weight'] + neighbors_second[0][2]['weight']
                E_aux.append((chosen_vertex, the_neighbor, {'weight': new_edge_weight}))
                E_new.remove(neighbor)
                E_new.remove(neighbors_second[0])
            # if there was no common neighbor
            else:
                E_aux.append((chosen_vertex, the_neighbor, {'weight': neighbor[2]['weight']}))
                E_new.remove(neighbor)
            
            # now we have to take care of the other vertex neighbors
        neighbors_second = [(u, v, d) for u, v, d in E_new 
                            if u == second_vertex or v == second_vertex]
        for neighbor in neighbors_second:
            if neighbor[0] == second_vertex:
                the_neighbor = neighbor[1]
            else:
                the_neighbor = neighbor[0]
            E_aux.append((chosen_vertex, the_neighbor, {'weight': neighbor[2]['weight']}))
            E_new.remove(neighbor)
        
        for edges in E_aux:
            E_new.append(edges)
            
        print("neighbors_second after: ")
        print(neighbors_second)
            

        
        
        # I haven't modified vertices weights because it is not needed 
        # all of the vertices are of the same weight so it does not play any role
        #E_aux.remove(edge_to_coarsen)
        # add edges to the new graph
        #chosen_vertex_neighbors =
        
        #print("adjacent edges: ")
        #print(adjacent_edges)
        
        # remove coarsened vertices and corresponding edges
        V.remove(chosen_vertex)
        print("second vertex:")
        print(second_vertex)
        V.remove(second_vertex)
        print(V)
        
file_name = 'graphs/graph10weighted.txt'

G = load_graph(file_name)
HEM_coarsening(G)

from collections import defaultdict
from random import randint
from random import seed

import time

def kargerMinCut(graph, total_edges):
    
    def rand_select_edge():
        
        edge_idx = randint(0, total_edges-1)
        # print(total_edges)
        for vertex, edges in graph.items():
            if len(edges) <= edge_idx:
                edge_idx -= len(edges)
            else:
                from_vertex = vertex
                to_vertex = edges[edge_idx]
        
        return (from_vertex, to_vertex)
    
    while len(graph) > 2:
        # print('number of vertices is: ', len(graph))

        v1, v2 = rand_select_edge()
        total_edges -= len(graph[v1])
        total_edges -= len(graph[v2])
        graph[v1].extend(graph[v2])

        ## merge into super vertex
        for vertex in graph[v2]:
            graph[vertex].remove(v2)
            graph[vertex].append(v1)

        ### remove self loops
        graph[v1] = list(filter(lambda x: x!=v1, graph[v1]))

        total_edges += len(graph[v1])
        graph.pop(v2)

    for edges in graph.values():
        min_cut = len(edges)
        # print(len(edges))
    
    return (graph, min_cut)




if __name__ == "__main__":
    
    txt_file = './kargerMinCut.txt'

    graph = {}
    total_edges = 0
    with open(txt_file, 'r') as f:
        for idx, line in enumerate(f):
            numbers = [int(number) for number in line.split()]
            graph[numbers[0]] = numbers[1:]
            total_edges += len(numbers[1:])

    # print(graph)
    print('total number of edges: ', total_edges)

    min_cut = 9999999

    for i in range(10000):
        graph, num = kargerMinCut(graph, total_edges)
        if num < min_cut:
            min_cut = num
    
    print('minimum cut is: ', min_cut)

    # print(graph)

























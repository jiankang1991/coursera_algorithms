
"""
In this programming problem you'll code up Prim's minimum spanning tree algorithm.

Download the text file below.

edges.txt
This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. 
You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. 
OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. 
The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). 
The superior approach stores the unprocessed vertices in the heap, as described in lecture. 
Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.


"""

from collections import defaultdict
import heapq


class Graph:

    def __init__(self, n):

        self.num_node = n
        self.nodes = set(range(1, n+1))
        self.edges = defaultdict(list)
        self.costs = defaultdict()
    
    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].append(to_node)
        self.costs[from_node,to_node] = cost


def mst_prim(graph, source_node = 1):

    X = set()
    X.add(source_node)
    MST = defaultdict(list)

    cost = 0

    while X != set(graph.nodes):

        cand_edge_costs = []

        for u_node in X:

            cand_edge_costs += [(u_node,v_node,graph.costs[u_node,v_node]) for v_node in graph.edges[u_node] if v_node not in X]
        
        min_edge = min(cand_edge_costs, key=lambda x: x[-1])

        # print(min_edge)

        MST[min_edge[0]].append(min_edge[1])
        
        X.add(min_edge[1])
        
        cost += min_edge[-1]

    return cost

def mst_prim_heap(graph, source_node = 1):

    q, visited = [(0, source_node, ())], set()

    total_cost = 0

    while visited != set(graph.nodes):

        (cost, v1, path) = heapq.heappop(q)

        if v1 not in visited:
            visited.add(v1)
            path = (v1, path)

            total_cost += cost

            for v2 in graph.edges[v1]:
                if v2 in visited:
                    continue

                heapq.heappush(q, (graph.costs[v1, v2], v2, path))

    return total_cost






if __name__ == "__main__":
    

    txt_file = './edges.txt'

    graph = Graph(500)

    with open(txt_file, 'r') as f:

        for line in f.readlines()[1:]:
            nums = line.split()
            ##### pay attention to here, the graph is undirected, so the edges should be added twice
            graph.add_edge(int(nums[0]), int(nums[1]), int(nums[2]))
            graph.add_edge(int(nums[1]), int(nums[0]), int(nums[2]))

    # print(graph.edges)


    print(mst_prim(graph))

    print(mst_prim_heap(graph))

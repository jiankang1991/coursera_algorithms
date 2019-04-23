""" 
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem. 
Here are data files describing three graphs:

g1.txt
g2.txt
g3.txt
The first line indicates the number of vertices and edges, respectively. 
Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number). 
NOTE: some of the edge lengths are negative. 
NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path". 
Precisely, you must first identify which, if any, of the three graphs have no negative cycles. 
For each such graph, you should compute all-pairs shortest paths and remember the smallest one 
(i.e., compute minu,v∈Vd(u,v), where d(u,v)d(u,v) denotes the shortest-path distance from uu to vv).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. 
If exactly one graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below. 
If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.

OPTIONAL: You can use whatever algorithm you like to solve this question. 
If you have extra time, try comparing the performance of different all-pairs shortest-path algorithms!

OPTIONAL: Here is a bigger data set to play with.

large.txt
For fun, try computing the shortest shortest path of the graph in the file above.

"""

from collections import defaultdict
from math import inf
from bellmanFord import BellmanFordFast, ReconstructPath
# from dijkstra_heap import dijkstra
from tqdm import tqdm

class Graph:
    def __init__(self, n):
        self.nodes = set(range(1, n+1))
        self.edges = defaultdict(list)
        self.distances = {}
        self.newNode = None
        self.nodesWeights = defaultdict()
        self.shortestPathPairs = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance
    
    def reweighting(self):
        
        self.newNode = max(self.nodes) + 1

        for node in self.nodes:
            self.add_edge(self.newNode, node, 0)

        self.nodes.add(self.newNode)

        # index is different 
        A, _ = BellmanFordFast(self, self.newNode - 1)

        for node in self.nodes:
            self.nodesWeights[node] = A[node-1]

        # delete edges and distances of newNode

        for node in self.edges[self.newNode]:
            self.distances.pop((self.newNode, node), None)

        self.edges.pop(self.newNode, None)
        self.nodes.remove(self.newNode)
        self.nodesWeights.pop(self.newNode, None)

        # reweighting the distances
        for fromNode, toNode in self.distances.keys():
            self.distances[fromNode, toNode] += self.nodesWeights[fromNode] - self.nodesWeights[toNode]
            assert self.distances[fromNode, toNode] >= 0

        # dijkstra algorithm

        for fromNode in self.nodes:
            
            A, B = BellmanFordFast(self, fromNode - 1)

            for idx, cost in enumerate(A):
                
                if cost == inf:
                    continue
                
                toNode = idx + 1
                # path = ReconstructPath(B, fromNode - 1, toNode - 1)
                # path.append(toNode - 1)
                # path = [a+1 for a in path]

                self.shortestPathPairs.append((fromNode, 
                                                toNode,
                                                cost-(self.nodesWeights[fromNode] - self.nodesWeights[toNode])
                                                ))

        
    def CalcShortestShortestPairs(self):

        
        fromNode, toNode, shortestCostP = min(self.shortestPathPairs, key = lambda x:x[2])

        print("from node {} to node {} has the shortest shortest path with the cost {}".format(fromNode, toNode, shortestCostP)) 





if __name__ == "__main__":
    
    txt_file = './g3.txt'

    graph = Graph(1000)

    with open(txt_file, 'r') as f:
        for line in f.readlines()[1:]:
            numbers = [num for num in line.split()]
            graph.add_edge(int(numbers[0]), int(numbers[1]), int(numbers[2]))

    # print(graph.distances)

    graph.reweighting()
    graph.CalcShortestShortestPairs()

    # print(graph.distances)





















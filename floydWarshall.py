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
import sys
from tqdm import tqdm

class Graph:
    def __init__(self, n):
        self.nodes = set(range(1, n+1))
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance
    

def FloydWarshall(graph):

    N = len(graph.nodes)
    # A = [[[0 for _ in range(N+1)] for _ in range(N)] for _ in range(N)]
    A = [[[0 for _ in range(2)] for _ in range(N)] for _ in range(N)]
    
    # initialization of predecessor
    B = [[i for _ in range(N)] for i in range(N)]


    # initialization
    for i in graph.nodes:
        
        woJList = list(graph.nodes)
        woJList.remove(i)

        for j in woJList:

            if j in set(graph.edges[i]):
                A[i-1][j-1][0] = graph.distances[i,j]

            else:
                A[i-1][j-1][0] = inf
                B[i-1][j-1] = -30000
    
    print("complete initialization")
    # print(B)

    for k in tqdm(range(1, N+1)):

        for i in range(N):
            for j in range(N):
                
                if A[i][j][(k-1) % 2] < A[i][k-1][(k-1) % 2]+A[k-1][j][(k-1) % 2]:
                    A[i][j][k % 2] = A[i][j][(k-1) % 2]
                else:
                    A[i][j][k % 2] = A[i][k-1][(k-1) % 2]+A[k-1][j][(k-1) % 2]
                    
                    if A[k-1][j][(k-1) % 2] != 0 and A[i][j][k % 2] != inf:
                        B[i][j] = B[k-1][j]


    # # check whether there is negative cycle
    for i in range(N):
        if A[i][i][-1] < 0:
            print("the graph has negative cycle")
            break

    ASlice = [[a[-1] for a in b] for b in A]
    return ASlice, B

def ComputeShortestShortestPath(A):
    
    N = len(A)
    
    minVal = 999999999
    edgeInfo = None

    for i in range(N):

        woJList = list(range(N))
        woJList.remove(i)

        for j in woJList:
            
            if A[i][j] < minVal:
                minVal = A[i][j]
                edgeInfo = (i,j)

    return minVal, edgeInfo

def ReconstructPath(fromNode, toNode, B):
    """ 
    recursively reconstruct the path from B
    """
    if fromNode == toNode:
        # print(fromNode)
        return [fromNode]
    
    elif B[fromNode][toNode] == -30000:
        print(fromNode, '-', toNode)
    
    else:
        path = ReconstructPath(fromNode, B[fromNode][toNode], B)
        path.append(toNode)
        # print(toNode,)
        return path




if __name__ == "__main__":
    
    ###########
    # txt_file = './g3.txt'

    # graph = Graph(1000)

    # with open(txt_file, 'r') as f:
    #     for line in f.readlines()[1:]:
    #         numbers = [num for num in line.split()]
    #         graph.add_edge(int(numbers[0]), int(numbers[1]), int(numbers[2]))

    # print(graph.edges)

    ###########
    # https://rosettacode.org/wiki/Floyd-Warshall_algorithm#Python

    graph = Graph(4)
    
    graph.add_edge(1, 3, -2)
    graph.add_edge(2, 1, 4)
    graph.add_edge(4, 2, -1)
    graph.add_edge(3, 4, 2)
    graph.add_edge(2, 3, 3)


    A, B = FloydWarshall(graph)
    print(A)
    minVal, (fromNode, toNode) = ComputeShortestShortestPath(A)
    print("min value: {} and min path from {} to {}".format(minVal, fromNode, toNode))
    # print(B)

    aa = ReconstructPath(1, 2, B)

    print(aa)








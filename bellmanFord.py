
from collections import defaultdict
from math import inf
from tqdm import tqdm

class Graph:
    def __init__(self, n):
        self.nodes = set(range(1, n+1))
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance





def BellmanFord(graph, sourceNode):
    """ 
        index and node should be pay attention here
    """
    N = len(graph.nodes)
    A = [[None for _ in range(N)] for _ in range(N+1)]
    B = [[None for _ in range(N)] for _ in range(N+1)]

    A[0][sourceNode] = 0
    

    for v in range(N):
        if v != sourceNode:
            A[0][v] = inf
    
    for i in tqdm(range(1, N+1)):
        for v in range(N):
            
            
            edges = list(filter(lambda x: x[-1]-1 == v, graph.distances.keys()))
            # print(edges)

            case2 = [A[i-1][edge[0]-1] + graph.distances[edge] for edge in edges]
            
            if len(case2) != 0:
                case2Min = min(case2)

                if A[i-1][v] < case2Min:
                    A[i][v] = A[i-1][v]
                    B[i][v] = B[i-1][v]
                else:
                    A[i][v] = case2Min
                    B[i][v] = edges[case2.index(case2Min)][0]-1
            else:
                A[i][v] = A[i-1][v]
                B[i][v] = B[i-1][v]

    for v in range(N):
        if A[-1][v] != A[-2][v]:
            print("the graph exists negative cycle")
            break
    # the last is used for checking wheter there is negative cycle inside
    # return i-1 
    return A[-2], B[-2]


def BellmanFordFast(graph, sourceNode):
    """
    https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/ 
    """
    N = len(graph.nodes)

    A = [inf for _ in range(N)]
    A[sourceNode] = 0

    B = [None for _ in range(N)]

    for i in tqdm(range(1, N)):

        for (fromNode, toNode), cost in graph.distances.items():

            if A[fromNode-1] != inf and A[fromNode-1] + cost < A[toNode-1]:
                A[toNode-1] = A[fromNode-1] + cost
                B[toNode-1] = fromNode-1

    for (fromNode, toNode), cost in graph.distances.items():
        if A[fromNode-1] != inf and A[fromNode-1] + cost < A[toNode-1]:
            print("the graph exists negative cycle")
            break

    return A,B








def ReconstructPath(B, sourceNode, endNode):

    if B[endNode] == sourceNode:
        return [sourceNode]
    elif B[endNode] == None:
        print("no direct path")
    else:
        path = ReconstructPath(B, sourceNode, B[endNode])
        path.append(B[endNode])
        return path








if __name__ == "__main__":
    
    ##########

    # graph = Graph(4)
    
    # graph.add_edge(1, 3, -2)
    # graph.add_edge(2, 1, 4)
    # graph.add_edge(4, 2, -1)
    # graph.add_edge(3, 4, 2)
    # graph.add_edge(2, 3, 3)


    # A, B = BellmanFord(graph, 0)

    # # print(B)
    # print("from source to every other node shortest length: ", A)
    
    # path = ReconstructPath(B, 0, 2)
    # path.append(2)

    # print("shortest path: ", path)


    ######

    txt_file = './dijkstraData.txt'

    graph = Graph(200)

    with open(txt_file, 'r') as f:
        for line in f:            
            numbers = [num for num in line.split()]
            for x in numbers[1:]:
                node2,length = x.split(',')
                graph.add_edge(int(numbers[0]), int(node2), int(length))


    # A, B = BellmanFord(graph, 0)
    A, B = BellmanFordFast(graph, 0)

    for i in [7-1,37-1,59-1,82-1,99-1,115-1,133-1,165-1,188-1,197-1]:

        path = ReconstructPath(B, 0, i)
        path.append(i)

        path = [a+1 for a in path]

        print("node {} path is {}".format(i+1, path) + " and distance is {}".format(A[i]))






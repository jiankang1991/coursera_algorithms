
import heapq
from collections import defaultdict



class Graph:
    def __init__(self, n):
        self.nodes = set(range(1, n+1))
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance

def dijkstra(graph, initial, end):
    
    q, visited, mins = [(0, initial, ())], set(), {initial:0}

    while q:
        (cost, v1, path) = heapq.heappop(q)

        if v1 not in visited:
            visited.add(v1)
            path = (v1, path)

            if v1 == end:
                return (cost, path)

            for v2 in graph.edges[v1]:
                if v2 in visited:
                    continue
                # prev = mins.get(v2, None)
                next_cost = graph.distances[v1, v2] + cost
                # # Not every edge will be calculated. The edge which can improve the value of node in heap will be useful.
                # if prev is None or next_cost < prev:
                #     mins[v2] = next_cost
                #     heapq.heappush(q, (next_cost, v2, path))
                mins[v2] = next_cost
                heapq.heappush(q, (next_cost, v2, path))
    
    return float("inf")







if __name__ == "__main__":
    

    txt_file = './dijkstraData.txt'

    graph = Graph(200)

    with open(txt_file, 'r') as f:
        for line in f:
            
            numbers = [num for num in line.split()]
            for x in numbers[1:]:
                node2,length = x.split(',')
                graph.add_edge(int(numbers[0]), int(node2), int(length))

    # print(graph.distances)
    # print(graph.edges)

    for t in [7,37,59,82,99,115,133,165,188,197]:

        print(dijkstra(graph, 1, t))
        
















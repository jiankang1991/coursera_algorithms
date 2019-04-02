from collections import defaultdict

class dijkstra:

    def __init__(self, graph, source_node, total_num_node, graph2=None):

        self.graph = graph
        self.graph2 = graph2
        self.X = [source_node]
        self.A = {source_node:0}
        self.B = {i:[] for i in range(1,total_num_node+1)}
        self.B[source_node] = [source_node]
        self.V = list(range(1,total_num_node+1))
        self.total_num_node = total_num_node
        self.source_node = source_node

        self.explored = {i:False for i in range(1, self.total_num_node+1)}

    def DFS(self):

        Q = [self.source_node]

        while len(Q) != 0:
            v = Q.pop()

            if not self.explored[v]:
                self.explored[v] = True
                Q.append(v)

                for j in self.graph2[v]:
                    if not self.explored[j]:
                        Q.append(j)
        
        # print(self.explored)
        unexplored_nodes = [k for k,v in filter(lambda x: x[1] is not True, self.explored.items())]
        print("unexplored nodes are: ", unexplored_nodes)


    def dijkstra_path_search(self):

        while set(self.X) != set(self.V):
            
            # print(sorted(self.X))
            node_pairs = []
            for node_x in self.X:

                node_pairs += [x for x in filter(lambda x: x[0]==node_x and x[1] not in set(self.X), self.graph.keys())] 
            
            # pay attention to the minimum distances are based on the dist from source to this node, not current
            paths = {x:self.graph[x] + self.A[x[0]] for x in node_pairs}
            min_path = min(paths, key=paths.get)


            # print("min path: ", self.graph[min_path])

            self.A[min_path[1]] = self.A[min_path[0]] + self.graph[min_path]
            self.X.append(min_path[1])

            extracted_path = self.B[min_path[0]].copy()
            self.B[min_path[1]] = extracted_path + [min_path[1]]

            # self.X = sorted(self.X)
        
        for i in range(1, self.total_num_node+1):
            
            if i in [7,37,59,82,99,115,133,165,188,197]:
                print("node {} path is {}".format(i, self.B[i]) + " and distance is {}".format(self.A[i]))

    







if __name__ == "__main__":
    
    ##############

    # graph1 = {(1,2):1, (1,3):4, (2,3):2, (2,4):6, (3,4):3}

    # graph2 = {(1,2):1, (1,8):2, (2,1):1, (2,3):1, (3,2):1, (3,4):1, (4,3):1, (4,5):1, (5,4):1, (5,6):1, (6,5):1, 
    #           (6,7):1, (7,6):1, (7,8):1, (8,7):1, (8,1):2}
    

    # dijkstra1 = dijkstra(graph2, 1, 8)
    # dijkstra1.dijkstra_path_search()


    #############
    txt_file = './dijkstraData.txt'

    graph = {}
    graph_DFS = defaultdict(list)

    total_num_node = 0
    with open(txt_file, 'r') as f:
        for line in f:
            
            numbers = [num for num in line.split()]
            
            for x in numbers[1:]:
                node2,length = x.split(',')
                graph[(int(numbers[0]), int(node2))] = int(length)
                graph_DFS[int(numbers[0])] += [int(node2)]

            total_num_node += 1
    # print("total number of nodes is: ", total_num_node)
    # print(graph_DFS)

    dijkstra2 = dijkstra(graph, 1,total_num_node, graph_DFS)
    # dijkstra2.DFS()
    dijkstra2.dijkstra_path_search()

















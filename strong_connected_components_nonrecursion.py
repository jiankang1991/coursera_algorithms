

from collections import defaultdict
from collections import Counter




class SCC:

    def __init__(self, graph, rev_graph, total_num_node):
        
        self.graph = graph
        self.rev_graph = rev_graph
        self.total_num_node = total_num_node
        # numbers of nodes processed so far, for finishing times in 1st pass
        self.t = 0
        # current source vertex, for leaders in 2nd pass
        self.s = None
        # finishing time
        self.F = defaultdict()
        self.explored = None
        self.leader = defaultdict()
        self.swap_F = None
        self.finished = {i:False for i in range(1, self.total_num_node+1)}

    def reset_explored(self):
        self.explored = {i:False for i in range(1, self.total_num_node+1)}


    def first_DFS_loop(self):

        self.reset_explored()
        for i in range(self.total_num_node, 0, -1):

            if not self.explored[i]:
                # self.s = i
                self.DFS_first_loop(self.rev_graph, i)

    def second_DFS_loop(self):

        self.reset_explored()
        # print(self.explored)
        self.swap_F = dict((v,k) for k,v in self.F.items())

        # print(self.swap_F)

        for i in range(self.total_num_node, 0, -1):
            if not self.explored[self.swap_F[i]]:
                self.s = self.swap_F[i]
                self.DFS_second_loop(self.graph, self.swap_F[i])


    def DFS_first_loop(self, graph, node):
        
        # self.explored[node] = True
        Q = [node]
        # finished = []

        while len(Q) != 0:
            # last in first out
            v = Q.pop()

            if not self.explored[v]:
                self.explored[v] = True
                Q.append(v)

                for j in graph[v]:
                    if not self.explored[j]:
                        Q.append(j)
            
            else:
                if not self.finished[v]:
                    self.t += 1
                    self.F[v] = self.t
                    self.finished[v] = True
                    # finished.append(v)

                    # print("node {} finishing time {}".format(v, self.F[v]))


    def DFS_second_loop(self, graph, node):
        
        # self.explored[node] = True
        Q = [node]
        # finished = []

        while len(Q) != 0:
            v = Q.pop()

            if not self.explored[v]:
                self.explored[v] = True
                self.leader[v] = self.s

                # print("node {} is of leader {}".format(v, self.s))

                Q.append(v)

                for j in graph[v]:
                    if not self.explored[j]:
                        Q.append(j)

            




if __name__ == "__main__":

    # graph = {7:[1], 1:[4], 4:[7], 9:[7,3], 6:[9], 3:[6], 8:[6,5], 2:[8], 5:[2]}
    # rev_graph = {1:[7], 4:[1], 7:[4,9], 3:[9], 9:[6], 6:[3,8], 8:[2], 2:[5], 5:[8]}

    # scc_test = SCC(graph, rev_graph, total_num_node=9)
    # scc_test.first_DFS_loop()
    # scc_test.second_DFS_loop()

    ####### assignment
    
    txt_file = './SCC.txt'
    
    graph = defaultdict(list)
    rev_graph = defaultdict(list)

    with open(txt_file, 'r') as f:
        for line in f:
            numbers = [int(num) for num in line.split()]
            graph[numbers[0]].append(numbers[1]) 
            rev_graph[numbers[1]].append(numbers[0])

    
    # # print(list(graph.items())[0:10])
    # print(dict(list(graph.items())[0:10]))

    print("total nodes: ", max(list(graph.keys())))

    scc = SCC(graph, rev_graph, total_num_node=max(list(graph.keys())))
    scc.first_DFS_loop()
    scc.second_DFS_loop()

    scc_counter = Counter(scc.leader.values())
    print("each SCC has number of nodes: ", sorted(list(scc_counter.values()), reverse=True)[:5])

















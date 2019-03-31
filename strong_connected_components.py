
from collections import defaultdict
from collections import Counter

# https://stackoverflow.com/questions/5061582/setting-stacksize-in-a-python-script/16248113#16248113
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

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

    def reset_explored(self):
        self.explored = {i:False for i in range(1, self.total_num_node+1)}

    def first_DFS_loop(self):

        self.reset_explored()
        for i in range(self.total_num_node, 0, -1):

            if not self.explored[i]:
                # self.s = i
                self.DFS(self.rev_graph, i)

    def second_DFS_loop(self):

        self.reset_explored()
        # print(self.explored)
        self.swap_F = dict((v,k) for k,v in self.F.items())

        # print(self.swap_F)

        for i in range(self.total_num_node, 0, -1):
            if not self.explored[self.swap_F[i]]:
                self.s = self.swap_F[i]
                self.DFS(self.graph, self.swap_F[i], first=False)


    def DFS(self, graph, node, first = True):
        self.explored[node] = True

        if not first:
            self.leader[node] = self.s
            # print("node {} is of leader {}".format(node, self.s))
        # arcs = {k:v for k,v in filter(lambda x: x[0]==node, graph.items())}

        for v in graph[node]:
            if not self.explored[v]:
                if first:
                    self.DFS(self.rev_graph, v)
                else:
                    self.DFS(self.graph, v, first=False)
        
        if first:
            self.t+=1
            self.F[node] = self.t
            print("node {} finishing time {}".format(node, self.F[node]))






if __name__ == "__main__":

    ############ example in the lecture

    graph = {7:[1], 1:[4], 4:[7], 9:[7,3], 6:[9], 3:[6], 8:[6,5], 2:[8], 5:[2]}
    rev_graph = {1:[7], 4:[1], 7:[4,9], 3:[9], 9:[6], 6:[3,8], 8:[2], 2:[5], 5:[8]}


    scc_test = SCC(graph, rev_graph, total_num_node=9)
    scc_test.first_DFS_loop()
    scc_test.second_DFS_loop()

    # print(scc_test.leader)
    total_SCC_num = len(list(set(scc_test.leader.values())))
    print("total SCC number of the graph is: ", total_SCC_num)

    SCC_counter = Counter(scc_test.leader.values())
    print("each SCC has number of nodes: ", SCC_counter.values())
    
    ############ assignment 
    # txt_file = './SCC.txt'
    
    # graph = defaultdict(list)
    # rev_graph = defaultdict(list)

    # with open(txt_file, 'r') as f:
    #     for line in f:
    #         numbers = [int(num) for num in line.split()]
    #         graph[numbers[0]].append(numbers[1]) 
    #         rev_graph[numbers[1]].append(numbers[0])

    
    # # # print(list(graph.items())[0:10])
    # # print(dict(list(graph.items())[0:10]))

    # print("total nodes: ", max(list(graph.keys())))

    # scc = SCC(graph, rev_graph, total_num_node=max(list(graph.keys())))
    # scc.first_DFS_loop()
    # scc.second_DFS_loop()

    # scc_counter = Counter(scc.leader.values())
    # print("each SCC has number of nodes: ", sorted(list(scc_counter.values()), reverse=True)[:5])


























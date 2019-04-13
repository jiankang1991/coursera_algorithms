""" In this programming problem and the next you'll code up the clustering algorithm from lecture for computing a max-spacing kk-clustering.

Download the text file below.

clustering1.txt
This file describes a distance function (equivalently, a complete graph with edge costs). It has the following format:

[number_of_nodes]

[edge 1 node 1] [edge 1 node 2] [edge 1 cost]

[edge 2 node 1] [edge 2 node 2] [edge 2 cost]

...

There is one edge (i,j)(i,j) for each choice of 1≤i<j≤n, where nn is the number of nodes.

For example, the third line of the file is "1 3 5250", indicating that the distance between nodes 1 and 3 (equivalently, the cost of the edge (1,3)) is 5250. 
You can assume that distances are positive, but you should NOT assume that they are distinct.

Your task in this problem is to run the clustering algorithm from lecture on this data set, where the target number kk of clusters is set to 4. What is the maximum spacing of a 4-clustering?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!

"""

from collections import defaultdict


class Cluster:

    def __init__(self, n):

        self.num_node = n
        self.nodes = set(range(1, n+1))
        self.edges = defaultdict(set)
        self.costs = defaultdict()
    
    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].add(to_node)
        self.edges[to_node].add(from_node)

        self.costs[from_node,to_node] = cost

    def MaxSpacingKClustering(self, K):

        

        while self.num_node != K:
            
            minDistNode = min(self.costs.items(), key=lambda x: x[-1])

            node1 = minDistNode[0][0]
            node2 = minDistNode[0][1]

            # assert node1 < node2

            # print("node 1 ", node1, "node 2", node2)
            # print(self.edges[1])

            for node in self.edges[node2]:

                # print(node, node2)

                # self.edges[node].remove(node2)

                if node in self.edges[node1]:

                    minCost = min(self.costs[tuple(sorted([node, node1]))], self.costs[tuple(sorted([node, node2]))])
                    self.costs[tuple(sorted([node, node1]))] = minCost

                else:
                    if node != node1:
                        self.edges[node1].add(node)
                        self.edges[node].add(node1)
                        self.costs[tuple(sorted([node, node1]))] = self.costs[tuple(sorted([node, node2]))]

                self.edges[node].remove(node2)
                self.costs.pop(tuple(sorted([node, node2])), None)
            

            self.edges.pop(node2, None)
            self.num_node -= 1


            











if __name__ == "__main__":
    
    txt_file = './clustering1.txt'

    cluster = Cluster(500)

    with open(txt_file, 'r') as f:

        for line in f.readlines()[1:]:
            nums = line.split()

            cluster.add_edge(int(nums[0]), int(nums[1]), int(nums[2]))


    # print(cluster.edges[1])

    cluster.MaxSpacingKClustering(K=4)

    print(cluster.costs)
    print(cluster.edges)



















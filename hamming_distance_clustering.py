
""" 
In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. 
So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.

The data set is below.

clustering_big.txt
The format is:

[# of nodes] [# of bits for each node's label]

[first bit of node 1] ... [last bit of node 1]

[first bit of node 2] ... [last bit of node 2]

...

For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

The distance between two nodes uu and vv in this problem is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels. 
For example, the Hamming distance between the 24-bit label of node #2 above and the label "0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of kk such that there is a kk-clustering with spacing at least 3? 
That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost. 
So you will have to be a little creative to complete this part of the question. 
For example, is there some way you can identify the smallest distances without explicitly looking at every pair of nodes?

"""

import collections
import itertools

from unionfind import UnionFind
from tqdm import tqdm

def flip(bit):

    return '0' if bit=='1' else '1'

def getNeiborhood(bits):

    for i in range(len(bits)):
        yield bits[:i] + (flip(bits[i]),) + bits[i+1:]
    
    for i, j in itertools.permutations(range(len(bits)), 2):
        if i < j:
            yield bits[0:i] + (flip(bits[i]),) + bits[i+1:j] + (flip(bits[j]),) + bits[j+1:]


def Clustering(nodes):

    UnionNodes = UnionFind(nodes.keys())


    for node in tqdm(nodes):

        for neighbour in getNeiborhood(node):

            if neighbour not in nodes:
                continue
            
            if not UnionNodes.connected(node, neighbour):
                UnionNodes.union(node, neighbour)

    
    return UnionNodes




if __name__ == "__main__":
    
    txtFile = './clustering_big.txt'

    data = collections.defaultdict()

    with open(txtFile, 'r') as f:
        for line in f.readlines()[1:]:
            nums = line.split()

            # data.append(tuple(nums))
            data[tuple(nums)] = tuple(nums)

    # print(data[:5])

    # cluster1 = Cluster(data)

    # print(cluster1.clustering())

    unionNodes = Clustering(data)

    print(unionNodes.n_comps)



















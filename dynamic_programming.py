
""" 
In this programming problem you'll code up the dynamic programming algorithm for computing a maximum-weight independent set of a path graph.

Download the text file below.

mwis.txt
This file describes the weights of the vertices in a path graph (with the weights listed in the order in which vertices appear in the path). It has the following format:

[number_of_vertices]

[weight of first vertex]

[weight of second vertex]

...

For example, the third line of the file is "6395702," indicating that the weight of the second vertex of the graph is 6395702.

Your task in this problem is to run the dynamic programming algorithm (and the reconstruction procedure) from lecture on this data set. 
The question is: of the vertices 1, 2, 3, 4, 17, 117, 517, and 997, which ones belong to the maximum-weight independent set? 
(By "vertex 1" we mean the first vertex of the graph---there is no vertex 0.) 
In the box below, enter a 8-bit string, where the ith bit should be 1 if the ith of these 8 vertices is in the maximum-weight independent set, and 0 otherwise. 
For example, if you think that the vertices 1, 4, 17, and 517 are in the maximum-weight independent set and the other four vertices are not, then you should enter the string 10011010 in the box below.

"""



class DynamicProgramming:

    def __init__(self, data):

        self.A = [0]*(len(data) + 1)
        self.weights = data
        
        self.A[1] = self.weights[0]

        self.path = []

    def MaxWeightedIndeSets(self):
        
        for idx, weight in enumerate(self.weights[1:]):

            self.A[idx+2] = max(self.A[idx+1], self.A[idx]+weight)


    def ReconstructPath(self):

        i = len(self.A)-1
        
        while i > 1:
            #### find the selecting path
            if self.A[i] == self.A[i-2] + self.weights[i-1]:
                self.path.append(i-1)
                i -= 2
            elif self.A[i] == self.A[i-1]:
                i -= 1
                continue
        ### check the base case of weights, 
        # if the third (3) node is included in the path, then the first should be also inside
        if i == 1:
            self.path.append(0)
            
        self.path = self.path[::-1]
        ### the index of assignment is from 1
        self.path = list(map(lambda x: x+1, self.path))

if __name__ == "__main__":

    txt_file = './mwis.txt'

    data = []

    with open(txt_file, 'r') as f:
        for line in f.readlines()[1:]:

            num = line.split()[0]

            data.append(int(num))
    
    dp = DynamicProgramming(data)
    dp.MaxWeightedIndeSets()
    dp.ReconstructPath()

    # print(dp.A)
    print(dp.path)

    for i in [1, 2, 3, 4, 17, 117, 517, 997]:
        print(i, i in dp.path)
















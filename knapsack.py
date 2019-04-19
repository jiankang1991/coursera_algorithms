""" 
In this programming problem and the next you'll code up the knapsack algorithm from lecture.

Let's start with a warm-up. Download the text file below.

knapsack1.txt
This file describes a knapsack instance, and it has the following format:

[knapsack_size][number_of_items]

[value_1] [weight_1]

[value_2] [weight_2]

...

For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.

You can assume that all numbers are positive. 
You should assume that item weights and the knapsack capacity are integers.

In the box below, type in the value of the optimal solution.

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. 
And then post them to the discussion forum!

"""
from collections import defaultdict

class KnapSackSmall:

    def __init__(self, values, sizes, capacity):

        self.A = [[0 for _ in range(capacity+1)] for _ in range(len(values)+1)]
        self.values = values
        self.sizes = sizes
        self.capacity = capacity
        self.optimalSets = []
    
    def ForwardKnapSack(self):

        for i in range(1, len(self.A)):
            # print(i)
            for x in range(0, self.capacity+1):
                
                if x - self.sizes[i-1] < 0:
                    self.A[i][x] = self.A[i-1][x]
                else:
                    self.A[i][x] = max(self.A[i-1][x], self.A[i-1][x-self.sizes[i-1]]+self.values[i-1])
        
        print("optimal solution: ", self.A[-1][-1])
    
    def ReconstructNodes(self):

        x = len(self.A[0]) - 1

        for i in range(len(self.A)-1, 0, -1):

            value = self.A[i][x]

            if value == self.A[i-1][x]:
                continue
            else:
                self.optimalSets.append(i)
                x -= self.sizes[i-1]

        # totalVal = 0
        # for v in self.optimalSets:
        #     totalVal += self.values[v-1]

        # print(totalVal)
        # print(self.A[-1][-1])


class KnapSackBig:

    def __init__(self, values, sizes, capacity):

        self.A = defaultdict()
        self.values = values
        self.sizes = sizes
        self.capacity = capacity
        self.optimalSets = []

        self.optimalSolution = None
        
        self.i = len(values)
        self.x = capacity

    def ForwardKnapSack(self, i, x):
        
        # print(A)
        # base case
        if i == 0 or x == 0:
            self.A[i,x] = 0
            return 0
            
        if x - self.sizes[i-1] < 0:
            # pay attention to the items already calculated
            if (i,x) not in self.A:
                self.A[i,x] = self.ForwardKnapSack(i-1, x)
            
            return self.A[i,x]
        else:
            # pay attention to the items already calculated
            if (i,x) not in self.A:
                self.A[i,x] = max(self.ForwardKnapSack(i-1, x),
                                  self.ForwardKnapSack(i-1, x-self.sizes[i-1])+self.values[i-1])
            
            return self.A[i,x]


    def OptimalSolution(self):
        
        self.optimalSolution = self.A[self.i, self.x]







if __name__ == "__main__":
    
    ######

    # txt_file = './knapsack1.txt'
    txt_file = './knapsack_big.txt'

    sizes = []
    values = []

    with open(txt_file, 'r') as f:

        nums = f.readline().split()

        capacity = int(nums[0])

        for line in f:
            nums = line.split()
            values.append(int(nums[0]))
            sizes.append(int(nums[1]))

    # print(len(sizes))
    # print(len(values))

    ###########

    # sizes = [4, 3, 2, 3]
    # values = [3, 2, 4, 4]
    # capacity = 6


    # knapSackSmallEx = KnapSackSmall(values, sizes, capacity)
    # print(len(knapSackSmallEx.A), len(knapSackSmallEx.A[0]))

    # knapSackSmallEx.ForwardKnapSack()
    # knapSackSmallEx.ReconstructNodes()

    # print(knapSackSmallEx.optimalSets)

    knapSackSmallEx = KnapSackBig(values, sizes, capacity)
    knapSackSmallEx.ForwardKnapSack(knapSackSmallEx.i, knapSackSmallEx.x)
    knapSackSmallEx.OptimalSolution()

    print(knapSackSmallEx.optimalSolution)

    











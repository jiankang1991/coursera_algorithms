
"""
Download the following text file:

algo1-programming_prob-2sum.txt
The goal of this problem is to implement a variant of the 2-SUM algorithm covered in this week's lectures.
The file contains 1 million integers, both positive and negative (there might be some repetitions!).
This is your array of integers, with the i^{th}i th row of the file specifying the i^{th}i th entry of the array.

Your task is to compute the number of target values tt in the interval [-10000,10000] (inclusive) 
such that there are distinct numbers x,yx,y in the input file that satisfy x+y=tx+y=t. 
(NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.
OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example, you could compare performance under the chaining and open addressing approaches to resolving collisions.

"""

from bisect import bisect_left, bisect_right






if __name__ == "__main__":
    

    txt_file = './algo1-programming_prob-2sum.txt'

    numberSet = set()

    with open(txt_file, 'r') as f:
        for line in f.readlines():
            numberSet.add(int(line))
    
    dist_num = 0

    numberSet = sorted(numberSet)

    numberTarget = set()

    for num in numberSet:
        low = bisect_left(numberSet, -10000-num)
        high = bisect_right(numberSet, 10000-num)

        yRange = numberSet[low:high]

        for y in yRange:
            if y!=num:
                numberTarget.add(num + y)
    
    print("num is {}".format(len(numberTarget)))























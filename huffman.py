
""" 
In this programming problem and the next you'll code up the greedy algorithm from the lectures on Huffman coding.

Download the text file below.

huffman.txt
This file describes an instance of the problem. It has the following format:

[number_of_symbols]

[weight of symbol #1]

[weight of symbol #2]

...

For example, the third line of the file is "6852892," indicating that the weight of the second symbol of the alphabet is 6852892. 
(We're using weights instead of frequencies, like in the "A More Complex Example" video.)

Your task in this problem is to run the Huffman coding algorithm from lecture on this data set. 
What is the maximum length of a codeword in the resulting Huffman code?

ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!


"""

from collections import Counter
import heapq

from collections import namedtuple

import time


symbol = namedtuple('symbol', ('weight', 'index'))


class Huffman:

    def __init__(self, data):
        
        self.codes = data
        # record the appearing times of each symbol when constructing the huffman tree
        self.symbols = [0] * len(data)

    def MetaSymbol(self, a, b):
        # merge the two nodes into meta node and keep track of the children nodes
        return '+'.join([a, b])

    def CompSymbol(self, symbol):
        # return the all the children composed in this metaNode
        return [a for a in symbol.split('+')]

    def HuffmanCoding(self):
        # recursive call of huffman coding alg
        self.codes.sort(key=lambda x: x[1])

        # print(self.codes)

        if len(self.codes) == 2:
            # base case
            components = [node for metaNode in (self.codes[0][0],self.codes[1][0]) for node in self.CompSymbol(metaNode)]

            for component in components:
                self.symbols[int(component)] += 1

            return None

        s1Code = self.codes.pop(0)
        s2Code = self.codes.pop(0)

        newCode = (self.MetaSymbol(s1Code[0],s2Code[0]), s1Code[1]+s2Code[1])
        
        self.codes.append(newCode)
        # extract all the leaf node components at this level
        components = [node for metaNode in (s1Code[0],s2Code[0]) for node in self.CompSymbol(metaNode)]
        # keep track of the appearing times of the nodes
        for component in components:
            self.symbols[int(component)] += 1

        self.HuffmanCoding()
    

class HuffmanHeap:

    def __init__(self, data):
        
        self.codes = data
        # record the appearing times of each symbol when constructing the huffman tree
        self.symbols = [0] * len(data)

        heapq.heapify(self.codes)

    def MetaSymbol(self, a, b):
        # merge the two nodes into meta node and keep track of the children nodes
        return '+'.join([a, b])

    def CompSymbol(self, symbol):
        # return the all the children composed in this metaNode
        return [a for a in symbol.split('+')]

    def HuffmanCoding(self):
        

        if len(self.codes) == 2:
            # base case
            components = [node for metaNode in (self.codes[0],self.codes[1]) for node in self.CompSymbol(metaNode.index)]

            for component in components:
                self.symbols[int(component)] += 1

            return None

        s1Code = heapq.heappop(self.codes)
        s2Code = heapq.heappop(self.codes)

        
        newCode = symbol(s1Code.weight + s2Code.weight, self.MetaSymbol(s1Code.index,s2Code.index))
        heapq.heappush(self.codes, newCode)

        components = [node for metaNode in (s1Code.index,s2Code.index) for node in self.CompSymbol(metaNode)]
        
        for component in components:
            self.symbols[int(component)] += 1

        self.HuffmanCoding()



    


if __name__ == "__main__":
    

    txt_file = './huffman.txt'

    ######### without heap
    data = []

    with open(txt_file, 'r') as f:
        for idx, line in enumerate(f.readlines()[1:]):
            
            num = line.split()[0]

            # data.append((str(idx), int(num)))
            data.append(symbol(int(num), str(idx)))

    # print(len(data))

    # startTime = time.time()

    # huffmanTest = Huffman(data)
    # huffmanTest.HuffmanCoding()

    # print(max(huffmanTest.symbols))
    # print(min(huffmanTest.symbols))
    # print("elasped time is: ", time.time() - startTime)

    ######## with heap 
    startTime = time.time()

    huffmanTestHeap = HuffmanHeap(data)
    huffmanTestHeap.HuffmanCoding()

    print(max(huffmanTestHeap.symbols))
    print(min(huffmanTestHeap.symbols))
    print("elasped time is: ", time.time() - startTime)



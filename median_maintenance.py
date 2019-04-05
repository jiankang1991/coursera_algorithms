
import heapq



class median_mantenance:

    def __init__(self):

        self.N = 0
        self.low_heap = []
        self.high_heap = []
        self.median = None
        self.sum_median = 0
        self.mod_median = 0

    def insert(self,x):
        
        if self.N == 0:
            heapq.heappush(self.low_heap, -x)
        
        else:

            min_low = min(self.low_heap)
            
            low = abs(min_low) > x

            if low:

                if len(self.low_heap) - len(self.high_heap) == 1:
                    # there is no function to pop max of heapq, try to turn it into a negative list
                    heap_pop_max = - heapq.heappop(self.low_heap)
                    # print(heap_pop_max)
                    
                    heapq.heappush(self.high_heap, heap_pop_max)
                    # heapq.heappush(self.low_heap, x)
                
                heapq.heappush(self.low_heap, -x)
            
            else:

                if len(self.high_heap) - len(self.low_heap) == 1:
                    heap_pop_min = - heapq.heappop(self.high_heap)
                    heapq.heappush(self.low_heap, heap_pop_min)
                    # heapq.heappush(self.high_heap,x)
                
                heapq.heappush(self.high_heap, x)

            if len(self.high_heap) - len(self.low_heap) == 1:
                heapq.heappush(self.low_heap, -heapq.heappop(self.high_heap))

            

        self.N += 1
        self.median = -min(self.low_heap)
        self.sum_median += self.median
        self.mod_median = self.sum_median % 10000

        # print("low heap len is {} high heap len is {} median is {}".format(
        #     len(self.low_heap), len(self.high_heap), self.median))
        
        # print(self.low_heap)
        # print(self.high_heap)



if __name__ == "__main__":

    # aa = [6331, 2793, 1640,9290,225,625,6195,2303,5685,1354,4292,7600,6447,4479,9046,7293,5147,1260,1386,6193]

    # stream_median = median_mantenance()

    # for a in aa:
    #     stream_median.insert(a)
    
    #######################
    txt_file = './Median.txt'

    stream_median = median_mantenance()

    with open(txt_file, 'r') as f:
        for line in f.readlines():
            # num = int(line.split()[0])
            # print(num)
            # stream_median.insert(num)
            stream_median.insert(int(line))

            print(stream_median.mod_median)










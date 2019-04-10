""" In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times..

Download the text file below.

jobs.txt
This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]

[job_1_weight] [job_1_length]

[job_2_weight] [job_2_length]

...

For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.

You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). 
Recall from lecture that this algorithm is not always optimal. 

IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. 
Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.

ADVICE: If you get the wrong answer, try out some small test cases to debug your algorithm (and post your test cases to the discussion forum).
"""
from collections import defaultdict
from collections import Counter

class job_schedule:

    def __init__(self, job_weights, job_lengths):

        self.job_weights = job_weights
        self.job_lengths = job_lengths

        self.job_schedule = []

        self.cost = 0
        self.completion_time = 0

    def minus_rule(self):

        self.cost = 0

        values = []
        for i in range(len(self.job_weights)):
            
            values.append(self.job_weights[i] - self.job_lengths[i])

        self.job_schedule = list(zip(self.job_weights, self.job_lengths, values))

        self.job_schedule.sort(key=lambda x: (x[-1], x[0]), reverse=True)

        # duplicate_values = [key for key, val in Counter(values).items() if val > 1]

        # # print(duplicate_values)
        # for val in duplicate_values:
            
        #     tmp_idx = [idx for idx, (a, b, c) in enumerate(self.job_schedule) if c==val]

        #     # print(tmp_idx)
        #     # print(self.job_schedule[tmp_idx[0]:tmp_idx[-1]+1])
        #     self.job_schedule[tmp_idx[0]:tmp_idx[-1]+1] = sorted(self.job_schedule[tmp_idx[0]:tmp_idx[-1]+1], key=lambda x: x[0], reverse=True)

    def ratio_rule(self):
        
        values = []
        for i in range(len(self.job_weights)):
            
            values.append(self.job_weights[i]/self.job_lengths[i])
        
        self.job_schedule = list(zip(self.job_weights, self.job_lengths, values))
        self.job_schedule.sort(key=lambda x: x[-1], reverse=True)

    
    def calc_cost(self):
        
        self.completion_time = 0
        self.cost = 0

        for weight, length, _ in self.job_schedule:

            self.completion_time += length

            self.cost += weight * self.completion_time
    









if __name__ == "__main__":
    
    txt_file = './jobs.txt'

    job_weights = []
    job_lengths = []
    with open(txt_file, 'r') as f:
        for line in f.readlines()[1:]:
            nums = line.split()
            # print(nums)
            job_weights.append(int(nums[0]))
            job_lengths.append(int(nums[-1]))

    # print(job_weights, job_lengths)  
    print(len(job_weights))  
    print(len(job_lengths))


    job_schedule_test = job_schedule(job_weights, job_lengths)
    job_schedule_test.minus_rule()
    job_schedule_test.calc_cost()

    print("minus total cost is: ", job_schedule_test.cost)

    job_schedule_test.ratio_rule()
    job_schedule_test.calc_cost()

    print("ratio total cost is: ", job_schedule_test.cost)

    # print(job_schedule_test.job_schedule)
    









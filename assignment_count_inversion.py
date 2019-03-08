

from count_inversion import recu_merge_sort


txt_file = './IntegerArray.txt'

with open(txt_file, 'r') as f:
    data = f.read().splitlines()


data = list(map(int, data))

print(data)

count = 0

count = recu_merge_sort(data)

print('the number of inversion is: ', count)



















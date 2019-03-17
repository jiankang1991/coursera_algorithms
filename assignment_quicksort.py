
from quicksort import quick_sort


txt_file = './QuickSort.txt'


with open(txt_file, 'r') as f:
    data = f.read().splitlines()


data = list(map(int, data))


count, sorted_data = quick_sort(data, 'median_of_three')

print('the number of comparison is: ', count)

# print('sorted result: ', sorted_data)













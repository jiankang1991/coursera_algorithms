
from statistics import median


# global count_number
# count_number = 0


def choose_pivot(a, option):

    if option == 'first':
        return a[0]
    elif option == 'final':
        return a[-1]
    elif option == 'median_of_three':
        return median([a[0], a[-1], a[(len(a)-1)//2]])




def quick_sort(a, option):

    # global count_number

    # print('partitioned： ', a)
    
    if len(a) > 1:
        
        pivot = choose_pivot(a, option)

        # print('pivot: ', pivot)

        ## preprocessing
        if option != 'first':
            #https://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list
            pivot_idx = a.index(pivot)
            a[0], a[pivot_idx] = a[pivot_idx], a[0]

        i = 1

        for j in range(1, len(a)):

            if a[j] < pivot:
                a[j], a[i] = a[i], a[j]
                i += 1
        
        # print('i:', i)

        a[i-1], a[0] = a[0], a[i-1]

        # print(a)
        ### if the pivot is the largest value, for slicing the left subarray, i should - 1
        # if i == len(a):
        #     # i -= 1

        #     a[:i-1] = quick_sort(a[:i-1], option)
        #     a[i-1:] = quick_sort(a[i-1:], option)

        # else:
        #     a[:i-1] = quick_sort(a[:i-1], option)
        #     a[i:] = quick_sort(a[i:], option)
        ## ignore the sorted item
        i -= 1
        count_less, a[:i] = quick_sort(a[:i], option)
        count_more, a[i+1:] = quick_sort(a[i+1:], option)
        

        # print('count_less a', a[:i])
        # print('count_more a', a[i:])
        
        # count_number += len(a) - 1
        # print(len(a) - 1)

        return len(a)-1+count_less+count_more, a
    
    else:
        return 0, a
    
                





if __name__ == "__main__":
    

    # a = [4, 5, 6, 7, 8]

    # print(choose_pivot(a, 'median_of_three'))

    a = [3, 8, 2, 5, 1, 4, 7, 6]

    # a = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7]

    count_number, sorted_a = quick_sort(a, 'final')

    print(count_number)
    print(sorted_a)















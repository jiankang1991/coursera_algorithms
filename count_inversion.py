""" count number of inversions in a list """

a = [1, 3, 5, 2, 4, 6]

b = [6, 5, 4, 3, 2, 1]


def recu_merge_sort(a):
    
    # print("splitting a: ", a)

    if len(a) > 1:
        
        counter = 0

        mid = len(a)//2
        left_half = a[:mid]
        right_half = a[mid:]

        left_counter = recu_merge_sort(left_half)
        right_counter = recu_merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a[k] = left_half[i]
                i += 1
            else:
                counter += len(left_half)-i
                a[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            a[k] = right_half[j]
            j += 1
            k += 1
        
        return left_counter + right_counter + counter
    
    else:
        return 0

inversion_num = recu_merge_sort(a)

print(inversion_num)
print(a)































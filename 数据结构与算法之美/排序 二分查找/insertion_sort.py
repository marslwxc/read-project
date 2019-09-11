from typing import List


def insertion_sort(alist):
    for i in range(1, len(alist)):
        value = alist[i]
        j = i - 1
        while j >= 0 and value < alist[j]:
            alist[j + 1], alist[j] = alist[j], alist[j + 1]
            j -= 1

    
array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
insertion_sort(array)
print(array)
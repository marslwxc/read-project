def selection_sort(alist):
    for i in range(len(alist)):
        min_value = alist[i]
        min_index = i
        for j in range(i, len(alist)):
            if alist[j] < min_value:
                min_index = j
                min_value = alist[j]
        alist[i], alist[min_index] = alist[min_index], alist[i]

    
array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
selection_sort(array)
print(array)
def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(i, len(alist)):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist

array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
bubble_sort(array)
print(array)
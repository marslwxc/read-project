"""
O(n) 时间复杂度内找到一组数据的第 K 大元素
"""
import random


def find_k(alist, k):
    k = len(alist) - k
    x = _find_k_between(alist, 0, len(alist) - 1, k)
    return x


def _find_k_between(alist, low, high, k):
    if low < high:
        a = _partition(alist, low, high)
        if a  == k:
            return alist[a]
        elif a < k:
            return _find_k_between(alist, a + 1, high, k)
        else:
            return _find_k_between(alist, low, a - 1, k)
    return False


def _partition(alist, low, high):
    pivot, i = alist[low], low
    for j in range(low + 1, high + 1):
        if alist[j] <= pivot:
            i += 1
            alist[i], alist[j] = alist[j], alist[i]
    alist[low], alist[i] = alist[i], alist[low]
    return i


array = [1,3,5,7,9,0,7,5,3,1,-2,6]
k = find_k(array, 2)
print(k)
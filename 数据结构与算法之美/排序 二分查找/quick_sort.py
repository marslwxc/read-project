from typing import List
import random


def quick_sort(alist: List):
    _quick_sort_between(alist, 0, len(alist) - 1)


def _quick_sort_between(alist, low, high):
    if low < high:
        k = random.randint(low, high)
        alist[k], alist[low] = alist[low], alist[k]
        q = _partition(alist, low, high)
        _quick_sort_between(alist, low, q - 1)
        _quick_sort_between(alist, q + 1, high)


def _partition(alist, low, high):
    pivot, i = alist[low], low
    for j in range(low + 1,high + 1):
        if alist[j] <= pivot:
            i += 1
            alist[i], alist[j] = alist[j], alist[i]
    alist[low], alist[i] = alist[i], alist[low]
    return i


def test_quick_sort():
    a1 = [3, 5, 6, 7, 8]
    quick_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)
from typing import List


def merge_sort(alist):
    _merge_sort_between(alist, 0, len(alist)-1)


def _merge_sort_between(alist, low, high):
    if low < high:
        mid = low + (high - low)//2
        _merge_sort_between(alist, low, mid)
        _merge_sort_between(alist, mid+1, high)
        _merge(alist, low, mid, high)


def _merge(alist, low, mid, high):
    i, j = low, mid+1
    result = []
    while i <= mid and j <= high:
        if alist[i] <= alist[j]:
            result.append(alist[i])
            i += 1
        else:
            result.append(alist[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    result.extend(alist[start:end + 1])
    alist[low:high+1] = result  

def test_merge_sort():
    a1 = [3, 5, 6, 7, 8]
    merge_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    merge_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    merge_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)
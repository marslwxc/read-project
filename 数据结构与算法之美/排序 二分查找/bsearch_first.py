def bsearch_first(a, n):
    low, high = 0, len(a)-1
    while low<=high:
        mid = low + (high - low) // 2
        if a[mid] > n:
            high = mid - 1
        if a[mid] < n:
            low = mid + 1
        if a[mid] == n:
            if mid == 0 or a[mid-1] != n:
                return mid
            else:
                high = mid - 1
    return False

a = [1,2,3,4,4,4,5]
n = bsearch_first(a, 4)
print(n)
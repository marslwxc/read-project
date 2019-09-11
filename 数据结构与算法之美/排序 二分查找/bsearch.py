def bsearch(alist, x):
    mid = len(alist) // 2
    while mid >= 0 and mid < len(alist):
        if alist[mid] > x:
            mid = mid // 2
        elif alist[mid] < x:
            mid = mid + (len(alist) - mid) // 2
        else:
            return mid
    return False


array = [1,2,3,4,5,6,7,8]
print(bsearch(array, 6)) 
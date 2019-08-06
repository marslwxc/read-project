
**二分查找针对的是一个有序的数据集合，查找思想有点类似分治思想。每次都通过跟区间的中间元素对比，将带查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为0**
![二分查找](https://static001.geekbang.org/resource/image/8b/29/8bce81259abf0e9a06f115e22586b829.jpg)
1. 二分查找的时间复杂度为O(nlogn)
2. 二分查找容易出错的三个地方
    1. 循环推出条件
    2. mid的取值
    3. low和high的更新


```python
def bsearch(a, n):
    low, high = 0, len(a)-1
    while low<=high:
        mid = low + (high - low) // 2
        if a[mid] == n:
            return mid
        if a[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```


```python
def bsearch(nums, target: int):
    return bsearch_internally(nums, 0, len(nums)-1, target)


def bsearch_internally(nums, low, high, target):
    if low > high:
        return -1

    mid = low+int((high-low) >> 2)
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return bsearch_internally(nums, mid+1, high, target)
    else:
        return bsearch_internally(nums, low, mid-1, target)
```

二分查找应用场景的局限性
1. 二分查找依赖的是顺序表结构，简单点说就是数组
2. 二分查找针对的是有序数据
3. 数据量太小不合适二分查找
4. 数据量太大也不适合二分查找

#### 变体一：查找第一个值等于给定值的元素
有序数据集合中存在重复的数据，我们希望找到第一个值等于给定值的数据

a[mid]跟要查找的value的大小关系有三种情况：大于、小于、等于。
1. 对于a[mid]>value的情况，我们需要更新high=mid-1；
2. 对于a[mid]<value的情况，我们需要更新low=mid+1。
3. 对于a[mid]=value的情况，
    1. 如果mid等于0，那这个元素已经是数组的第一个元素，那就是我们要找的
    2. 如果mid不等于0，但a[mid]的前一个元素a[mid-1]不等于value，也说明a[mid]就是我们要找的等一个值等于给定值的元素
    3. 如果mid的前一个元素也等于value，那说明这个数不是第一个值。那我们就更新high=mid-1


```python
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
```

    3
    

#### 变体二：查找最后一个等于给定值的元素
1. 省略
2. 省略
3. a[mid] == value
    1. 如果a[mid]是数组最后一个元素或者a[mid+1]!=value，这就是我么要的值
    2. 如果a[mid+1]也等于value，那么low=mid+1


```python
def bsearch_first(a, n):
    low, high = 0, len(a)-1
    while low<=high:
        mid = low + (high - low) // 2
        if a[mid] > n:
            high = mid - 1
        if a[mid] < n:
            low = mid + 1
        if a[mid] == n:
            if mid == 0 or a[mid+1] != n:
                return mid
            else:
                low = mid + 1
    return False

a = [1,2,3,4,4,4,5]
n = bsearch_first(a, 4)
print(n)
```

    5
    

#### 变体三：查找第一个大于等于给定值的元素
1. 如果a[mid]小于value，那更新low=mid+1
2. 如果a[mid]大于等于value
    1. 如果a[mid]前面已经没有元素，或者前面的值小于value，那么a[mid]就是要找的元素
    2. 如果a[mid]前面的元素也大于等于value，更新high=mid-1


```python
def bsearch_first(a, n):
    low, high = 0, len(a)-1
    while low<=high:
        mid = low + (high - low) // 2
        if a[mid] < n:
            low = mid + 1
        if a[mid] >= n:
            if mid == 0 or a[mid-1] < n:
                return mid
            else:
                high = mid - 1
    return False

a = [1,2,3,4,4,4,5]
n = bsearch_first(a, 4)
print(n)
```

    3
    

#### 变体四：查找最后一个小于等于给定值的元素
1. 如果a[mid]大于于value，那更新high=mid-1
2. 如果a[mid]小于于等于value
    1. 如果a[mid]后面已经没有元素，或者后面的值大于value，那么a[mid]就是要找的元素
    2. 如果a[mid]后面的元素也小于等于value，更新low=mid+1


```python
def bsearch_first(a, n):
    low, high = 0, len(a)-1
    while low<=high:
        mid = low + (high - low) // 2
        if a[mid] > n:
             high = mid - 1
        if a[mid] <= n:
            if mid == 0 or a[mid+1] > n:
                return mid
            else:
                low = mid + 1
    return False

a = [1,2,3,4,4,4,5]
n = bsearch_first(a, 4)
print(n)
```

    5
    


```python

```

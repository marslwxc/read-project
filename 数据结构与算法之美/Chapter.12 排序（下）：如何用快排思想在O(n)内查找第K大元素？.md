
# 分治思想
1. 分治思想：分治，顾名思义，就是分而治之，将一个大问题分解成小的子问题来解决，小的子问题解决了，大问题也就解决了
2. 分治与递归的区别：分治算法一般都是用递归来实现的。分治是一种解决问题的处理思想，递归是一种编程技巧。

# 归并排序
## 算法原理
先把数组从中间分成前后两部分，然后对前后两部分分别进行排序，再将排序号的两部分分别进行排序，再将排序好的两部分合并到一起，这样整个数组就有序了。如何用递归实现归并排序呢？写递归代码的技巧就是分写得出递归公式，然后找到终止条件，最后将递推公式翻译成递归代码。递推公式怎么写？如下递推公式
```
merge_sort(p...r) = merge(merge_sort(p...1),merge_sort(q+1...r))
```
终止条件：p>=r
![](https://static001.geekbang.org/resource/image/db/2b/db7f892d3355ef74da9cd64aa926dc2b.jpg)
## 代码实现


```python
from typing import List

def merge_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return a
    mid = length//2
    left_list = merge_sort(a[:mid])
    right_list = merge_sort(a[mid:])
    left_point, right_point = 0, 0
    result = []
    while left_point < len(left_list) and right_point < len(right_list):
        
        if left_list[left_point] < right_list[right_point]:
            result.append(left_list[left_point])
            left_point += 1
        else:
            result.append(right_list[right_point])
            right_point += 1
    
    result += left_list[left_point:]
    result += right_list[right_point:]
    return result

llist = [1,3,5,7,9,0,8,6,4,2]
print(merge_sort(llist))
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    


```python
def merge_sort(a: List[int]):
    _merge_sort_between = (a, 0, len(a)-1)
    
    
def _merge_sort_between(a: List[int], low: int, high: int):
    # The indices are inculsivve for both low and high
    if low < high:
        mid = low + (high-low)//2
        _merge_sort_between(a, low, mid)
        _merge_sort_between(a, mid+1, high)
        _merge(a, low, mid, high)
        
def _merge(a: List[int], low: int, mid: int, high: int):
    # a[low:mid], a[mid+1, high] are sorted.
    i, j = low, mid+1
    tmp = []
    while i<mid and j<high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high+1] = tmp
    

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
```

    [3, 5, 6, 7, 8]
    [2, 2, 2, 2]
    [4, 3, 2, 1]
    [5, -1, 9, 3, 7, 8, 3, -2, 9]
    

## 性能分析
### 算法稳定性
归并排序稳不稳定的关键要看merge()函数，也就是两个子数组合并成一个有序数组的那部分代码。再合并的过程中，如果A[p...q]和A[q+1...r]之间有值相的元素，那我们就可以像伪代码中的那样，先把A[p...q]中的元素放入tmp数组，这样就保证了值相同的元素，子啊合并前后的先后顺序不变。所以，**归并排序是一种稳定的排序算法。**
### 时间复杂度
分析归并排序的时间复杂度就是分析递归代码的时间复杂度。递归的适用场景是一个问题a可以分解为多个子问题b、c。问题b、c解决之后，再把b、c的结果合并成a的结果。若定义求解问题a的时间是T（a),则求解问题b、c的时间分别是T(b)、T(c)。那就可以得到这样的递推公式：T(a) = T(b) + T(c) + K，其中K等于将两个子问题b、c的结果合并成问题a的结果所消耗的时间。这里有一个重要的结论：不仅递归求解的问题可以写成递推公式，递归代码的时间复杂度也可以写成递推公式。套用这个公式，那么归并排序的时间复杂度就可以表示为：
T(1) = C； n=1 时，只需要常量级的执行时间，所以表示为 C。
T(n) = 2*T(n/2) + n； n>1，其中n就是merge()函数合并两个子数组的的时间复杂度O(n)。
T(n) = 2*T(n/2) + n
     = 2*(2*T(n/4) + n/2) + n = 4*T(n/4) + 2*n
     = 4*(2*T(n/8) + n/4) + 2*n = 8*T(n/8) + 3*n
     = 8*(2*T(n/16) + n/8) + 3*n = 16*T(n/16) + 4*n
     ......
     = 2^k * T(n/2^k) + k * n
     ......
当T(n/2^k)=T(1) 时，也就是 n/2^k=1，我们得到k=log2n。将k带入上面的公式就得到T(n)=Cn+nlog2n。如用大O表示法，T(n)就等于O(nlogn)。所以，**归并排序的是复杂度时间复杂度就是O(nlogn)。**
### 空间复杂度
归并排序算法不是原地排序算法，空间复杂度是O(n)
为什么？因为归并排序的合并函数，在合并两个数组为一个有序数组时，需要借助额外的存储空间。为什么空间复杂度是O(n)而不是O(nlogn)呢？如果我们按照分析递归的时间复杂度的方法，通过递推公式来求解，那整个归并过程需要的空间复杂度就是O(nlogn)，但这种分析思路是有问题的！因为，在实际上，递归代码的空间复杂度并不是像时间复杂度那样累加，而是这样的过程，即在每次合并过程中都需要申请额外的内存空间，但是合并完成后，临时开辟的内存空间就被释放掉了，在任意时刻，CPU只会有一个函数在执行，也就只会有一个临时的内存空间在使用。临时空间再大也不会超过n个数据的大小，所以**空间复杂度是O(n)。**

# 快速排序
## 算法原理
如果要排序数组中下标从p到r之间的一组数据，选择p到r之间的任意一个数据作为pivot。然后遍历p到r之间的数据，将小于pivot的放到左边，将大于pivot的放到右边，将pivot放到中间。经过这一步之后，数据p到r之间的数据就分成了3部分，前面p到q-1之间都是小于povit的，中间是povit，后面q+1到r之间是大于povit的。根据分治、递归的处理思想，我们可以用递归排序下标从p到q-1之间的数据和下标q+1到r之间的数据，直到区间缩小为1，就说明所有的数据都有序了。
```
递推公式：quick_sort(p…r) = quick_sort(p…q-1) + quick_sort(q+1, r)
终止条件：p >= r
```
![](https://static001.geekbang.org/resource/image/66/dc/6643bc3cef766f5b3e4526c332c60adc.jpg)
![](https://static001.geekbang.org/resource/image/aa/05/aa03ae570dace416127c9ccf9db8ac05.jpg)
## 代码实现


```python
def q_sort(a: List[int], first, last):
    if first >= last:
        return
    mid_value = a[first]
    low = first
    high = last
    while low<high:
        while low<high and a[high]>=mid_value:
            high -= 1
        a[low] = a[high]
        while low<high and a[low]<=mid_value:
            low += 1
        a[high] = a[low]
    a[low] = mid_value
    q_sort(a, first, low-1)
    q_sort(a, low+1, last)
    return a

list = [11, 22, 33, 23, 56, 54, 77, 90, 89]
print(q_sort(list, 0, len(list)-1))
```

    [11, 22, 23, 33, 54, 56, 77, 89, 90]
    


```python
import random


def quick_sort(a: List[int]):
    _quick_sort_between(a, 0, len(a)-1)
    
    
def _quick_sort_between(a: List[int], low: int, high: int):
    if low < high:
        #get a random position as the pivot
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]
        
        m = _partition(a, low, high) #a[m] is in final position
        _quick_sort_between(a, low, m-1)
        _quick_sort_between(a, m+1, high)
        
        
def _partition(a: List[int], low: int, high: int):
    povit, j = a[low], low
    for i in range(low+1, high+1):
        if a[i] <= povit:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[low], a[j] = a[j], a[low]
    return j


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
```

    [3, 5, 6, 7, 8]
    [2, 2, 2, 2]
    [1, 2, 3, 4]
    [-2, -1, 3, 3, 5, 7, 8, 9, 9]
    

## 性能分析
### 算法稳定性
因为分区过程中设计交换操作，如果数组中有两个8，其中一个是pivot，经过分区处理后，后面的8就有可能放到另一个8的前面，先后顺序就颠倒了，所以快速排序是不稳定的排序算法。比如数组[1,2,3,9,8,11,8]，取后面的8作为pivot，那么分区后就会将后面的8与9进行交换。
### 时间复杂度
快排也是用递归实现的，所以时间复杂度也可以用递推公式表示。
如果每次分区操作都能正好把数组分成大小接近相等的两个小区间，那快排的时间复杂度递推求解公式跟归并的相同。
```
T(1) = C； n=1 时，只需要常量级的执行时间，所以表示为 C。
T(n) = 2*T(n/2) + n； n>1
```
所以，**快排的时间复杂度也是O(nlogn)。**
如果数组中的元素原来已经有序了，比如1，3，5，6，8，若每次选择最后一个元素作为pivot，那每次分区得到的两个区间都是不均等的，需要进行大约n次的分区，才能完成整个快排过程，而每次分区我们平均要扫描大约n/2个元素，这种情况下，快排的时间复杂度就是O(n^2)。
前面两种情况，一个是分区及其均衡，一个是分区极不均衡，它们分别对应了快排的最好情况时间复杂度和最坏情况时间复杂度。那快排的平均时间复杂度是多少呢？T(n)大部分情况下是O(nlogn)，只有在极端情况下才是退化到O(n^2)，而且我们也有很多方法将这个概率降低。
### 空间复杂度
**快排是一种原地排序算法，空间复杂度是O(1)**




对于一个排序算法执行效率的分析，一般会从几个方面衡量：
1. 最好情况、最坏情况、平均情况时间复杂度
2. 时间复杂度的系数、常数、低阶
3. 比较次数和交换次数

原地排序(Sorted inplace):就是指空间复杂度为O(1)的排序算法。

稳定性：如果排序的序列中存在值相等的元素，经过排序之后，想等元素之间原有的先后顺序不变。这样的算法叫做**稳定排序算法**，否则叫做**不稳定排序算法**。

有序度：指数组中具有有序关系的元素对的个数。对于一个完全有序的n元素数组，**有序度就是n*(n-2)/2，也叫做满有序。满有序-有序度=逆序度，也是一个数组排序需要交换元素的次数。**

### 冒泡排序(Bubble Sort)
冒泡排序只会操作相邻的两个数据。每次冒泡操作都会对相邻的两个元素进行比较，看是否满足大小关系要求。如果不满足就让它俩互换。一次冒泡会让至少一个元素移动到它应该的位置，重复n次，就完成了n个数据的排序工作。
![冒泡排序过程](https://static001.geekbang.org/resource/image/40/e9/4038f64f47975ab9f519e4f739e464e9.jpg)
![冒泡排序过程](https://static001.geekbang.org/resource/image/92/09/9246f12cca22e5d872cbfce302ef4d09.jpg)
![冒泡排序](https://static001.geekbang.org/resource/image/a9/e6/a9783a3b13c11a5e064c5306c261e8e6.jpg)
1. 冒泡排序的空间复杂度是O(1)，是一个原地排序算法
2. 冒泡排序是稳定的排序算法
3. 冒泡排序的平均时间复杂度是O(n2)


```python
def bubble_sort(num):
    l = len(num)
    if l <= 0:return 
    for i in range(l):
        for j in range(i+1,l):
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]
    return num
                
                
array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
bubble_sort(array)
print(array)
```

    [-1, 2, 4, 5, 6, 6, 7, 8, 10]
    

### 插入排序(Insertion Sort)
首先，将数组中的数据分为两个区间，**已排序区间**和**未排序区间**。初始已排序区间只有一个元素，就是数组的第一个元素。插入算法的核心思想是取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入，并保证已排序区间数据一直有序。重复这个过程，直到未排序区间中元素为空，算法结束。
![插入排序](https://static001.geekbang.org/resource/image/b6/e1/b60f61ec487358ac037bf2b6974d2de1.jpg)
插入排序包含两种操作，一种是元素的比较，一种是元素的移动。
1. 插入排序的空间复杂度是O(1)，是原地算法
2. 插入排序是稳定的排序算法
3. 插入排序的平均时间复杂度是O(n2)


```python
# 插入排序
def insertion_sort(lists):
    l = len(lists)
    for i in range(1, l):
        value = lists[i]
        j = i - 1
        while j >= 0 and lists[j] > value:
            lists[j+1] = lists[j]
            j -= 1
        lists[j+1] = value

array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
insertion_sort(array)
print(array)
```

    [-1, 2, 4, 5, 6, 6, 7, 8, 10]
    

### 选择排序（Selection Sort）
选择排序算法的实现思路类似于插入排序，将数组分为已排序分区和未排序分区。选择排序每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾
![选择排序](https://static001.geekbang.org/resource/image/32/1d/32371475a0b08f0db9861d102474181d.jpg)
1. 选择排序的空间复杂度为O(1)，是原地排序算法
2. 平均时间复杂度是O(n2)
3. 选择排序是一种不稳定的排序算法


```python
# 选择排序
def selection_sort(a):
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        min_index = i
        min_val = a[i]
        for j in range(i, length):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        
array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
selection_sort(array)
print(array)
```

    [-1, 2, 4, 5, 6, 6, 7, 8, 10]
    

### 归并排序（Merge Sort）
如果要排序一个数组，先把数组从中间分成前后两部分，然后对前后两部分分别排序，再将排好序的两部分合并到一起。
![归并排序](https://static001.geekbang.org/resource/image/db/2b/db7f892d3355ef74da9cd64aa926dc2b.jpg)
归并排序使用的是**分治思想**。就是分而治之，将一个大问题分解成小的子问题来解决。

分治是一种解决问题的处理思想，递归是一种编程技巧
1. 归并排序是一个稳定的排序算法
2. 归并排序的时间复杂度是O(nlogn)
3. 归并排序的时间复杂度是O(n)


```python
# 归并排序
def merge_sort(lists):
    l = len(lists)
    mid = l // 2
    left_list = lists[:mid]
    right_list = lists[mid:]
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

    [0, 1, 3, 5, 7, 8, 6, 4, 2, 9]
    

### 快速排序(QuickSort)
快排的思想：如果要排序数组中下标从p到r之间的一组数据，选择p到r之间的任意一个数据作为pivot(分区点)。之后遍历p到r之间的数据，将小于pivot的放到左边，将大于pivot的放到右边，将pivot放到中间。经过这一步骤之后，数组p到r之间的数据就被分为了三个部分，前面p到q-1之间都是小于pivot的，中间是pivot，后面q+1到r之间是大于pivot的。
![快速排序](https://static001.geekbang.org/resource/image/4d/81/4d892c3a2e08a17f16097d07ea088a81.jpg)
![快排分区过程](https://static001.geekbang.org/resource/image/08/e7/086002d67995e4769473b3f50dd96de7.jpg)
1. 快排是一种原地、不稳定的算法
2. 快排的时间复杂度是O(nlogn)


```python
# 快速排序
def quick_sort(a):
    _quick_sort_between(a, 0, len(a)-1)
    
def _quick_sort_between(a, low, high):
    if low>high: return
    m = _pivot(a, low, high)
    _quick_sort_between(a, low, m-1)
    _quick_sort_between(a, m+1, high)
    
def _pivot(a, low, high):
    pivot, j = a[low], low
    for i in range(low+1, high+1):
        if a[i] <= pivot:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[low], a[j] = a[j], a[low]
    return j
```


```python
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
    

### 桶排序
桶排序的核心思想是将要排序的数据分到几个有序的桶里，每个桶里的数据再单独进行排序。桶内排完序之后，再把每个桶里的数据按照顺序依次取出，组成的序列就是有序的了。
![桶排序](https://static001.geekbang.org/resource/image/98/ae/987564607b864255f81686829503abae.jpg)
**桶排序比较适合用在外部排序中**。所谓的外部排序就是数据存储在外部磁盘中，数据量大，内存有限，无法将数据全部加载到内存中。

### 计数排序
要使用计数排序排序n个数据时，当n个数据所处的范围并不大的时候，比如最大值是k，我们就可以把数据划分成k个桶。每个桶内的数据值都是相同的，省掉了桶内排序的时间

计数排序只能用在数据范围不大的场景中，如果数据范围k比要排序的数据n大得多，就不适合用计数排序了。而且，计数排序只能给非负整数排序，如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数。

### 基数排序
基数排序对要排序的数据是有要求的，需要可以分割出独立的“位”来比较，而且位之间有递进关系，如果a数据的高位比b数据大，那剩下的低位就不用比较了。除此之外，每一位的数据范围不能太大，要可以用先行排序算法来排序，否则，时间复杂度就无法达到O(n)了。

### 排序优化
1. 选择合适的排序算法
![算法比较](https://static001.geekbang.org/resource/image/1f/fd/1f6ef7e0a5365d6e9d68f0ccc71755fd.jpg)
2. 如何优化快速排序
为什么最坏情况下快速排序的时间复杂度是O(n2)呢？如果数据原来就是有序的或者接近有序的，每次分区点都选择最后一个数据，那快速排序算法就会变得非常糟糕，时间复杂度就会退化为O(n2)。**这种O(n2)时间复杂度出现的主要原因是因为我们分区点选择不够合理**
    1. 三数取中法
    2. 随机法


```python

```

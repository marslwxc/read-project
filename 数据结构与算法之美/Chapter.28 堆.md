
堆排序是一种**原地的、时间复杂度为O(nlogn)的**排序算法。

堆是一种特殊的树，只要满足一下两点，它就是一个堆：
1. 堆是一个完全二叉树
2. 堆中每一个节点的值都必须大于等于（或小于等于）其子树中每个节点的值
![](https://static001.geekbang.org/resource/image/4d/1e/4d349f57947df6590a2dd1364c3b0b1e.jpg)
数组中下标为 i 的节点的左子节点，就是下标为 i\*2 的节点，右子节点就是 i\*2+1 的节点，父节点就是 i/2 的节点。

#### 往堆中插入一个元素
当在堆的末尾处插入一个数据时，为了满足堆的特性，需要进行调整，让其重新满足堆的特性，这个过程被叫做**堆化(heapify)**。堆化有两种，从下往上和从上往下。

堆化很简单，就是顺着节点所在的路径，向上或向下，对比，然后交换。可以让新插入的节点与父节点对比大小。如果不满足子节点小于等于父节点的大小关系，就互换两个节点。一直重复这个过程，直到父子节点之间满足刚说的那种大小关系。
![](https://static001.geekbang.org/resource/image/e3/0e/e3744661e038e4ae570316bc862b2c0e.jpg)

#### 删除堆顶元素
从堆的定义的第二条中，任何节点的值都大于等于(或小于等于)子树节点的值，可以发现，堆顶元素存储的就是堆中数据的最大值或者最小值。
1. 假设我们构造的是大顶堆，堆顶元素就是最大的元素。当我们删除堆顶元素之后，就需要把第二大的元素放到堆顶，那第二大元素肯定会出现在左右子节点中。然后我们再迭代地删除第二大节点，一次类推，直到叶子节点被删除。
![](https://static001.geekbang.org/resource/image/59/81/5916121b08da6fc0636edf1fc24b5a81.jpg)
2. 把最后一个节点放到堆顶，然后利用同样的父子节点对比方法。对于不满足父子节点大小关系的，互换两个节点，并且重复进行这个过程，直到父子节点之间满足大小关系为止。**这就是从上往下的堆化方法**。因为我们移除的是数组中最后一个元素，而在堆化过程中，都是互换操作，不会出现数组中的“空洞”，所以这种方法堆化之后的结果，肯定满足完全二叉树的特性。
![](https://static001.geekbang.org/resource/image/11/60/110d6f442e718f86d2a1d16095513260.jpg)

**往堆中插入一个元素和删除堆顶元素的时间复杂度都是O(logn)**

#### 基于堆实现排序
借助于堆实现的排序算法，叫做堆排序。这种排序方法的时间复杂度是O(nlogn)，稳定且是原地排序算法。
1. 建堆：首先，将数组原地建成一个堆
    1. 第一种方法：借助往堆中插入一个元素的思路。可以假设，起初堆中只包含一个数据，就是下标为1的数据。然后，调用插入操作，将下标从2开始的数据依次插入到堆中。
    2. 第二种方法：是从后往前处理数据，并且每个数据都是从上往下堆化。
    ![](https://static001.geekbang.org/resource/image/50/1e/50c1e6bc6fe68378d0a66bdccfff441e.jpg)
2. 排序
    数组中的第一个元素就是堆顶，也就是最大的元素。把它跟最后一个元素交换，那最大元素就放到了下标为n的位置。然后再通过堆化的方法，将剩下的n-1个元素重新构建成堆。堆化完成之后，再取堆顶的元素，放到n-1的位置，一直重复这个过程，直到最后堆中只剩下下标为1的一个元素。
    ![](https://static001.geekbang.org/resource/image/23/d1/23958f889ca48dbb8373f521708408d1.jpg)
- 堆排序的整体时间复杂度是O(nlogn)


```python
import math
import random


class BinaryHeap:
    """
    大顶堆
    """
    def __init__(self, data=None, capacity=100):
        self._data = []
        self._capacity = capacity
        if type(data) is list:
            if len(data) > self._capacity:
                raise Exception('Heap oversize, capacity:{}, data size:{}'.format(self._capacity, len(data)))
            self._type_assert(data)
            self._data = data

        self._length = len(self._data)

    def heapify(self):
        """
        堆化
        :return:
        """
        self._heapify(self._data, self._length-1)

    def _heapify(self, data, tail_idx):
        """
        堆化内部实现
        :param data: 需要堆化的数据
        :param tail_idx: 尾元素的索引
        :return:
        """
        # heapify data[:tail_idx+1]
        if tail_idx <= 0:
            return

        # idx of the Last Parent node
        lp = (tail_idx - 1) // 2

        for i in range(lp, -1, -1):
            self._heap_down(data, i, tail_idx)

    @staticmethod
    def _heap_down(data, idx, tail_idx):
        """
        将指定的位置堆化
        :param data: 需要堆化的数据
        :param idx: data: 中需要堆化的位置
        :param tail_idx: 尾元素的索引
        :return:
        """
        assert type(data) is list

        lp = (tail_idx - 1) // 2
        # top-down
        while idx <= lp:
            # Left and Right Child index
            lc = 2 * idx + 1
            rc = lc + 1

            # right child exists
            if rc <= tail_idx:
                tmp = lc if data[lc] > data[rc] else rc
            else:
                tmp = lc

            if data[tmp] > data[idx]:
                data[tmp], data[idx] = data[idx], data[tmp]
                idx = tmp
            else:
                break

    def insert(self, num):
        """
        插入
        :param num:
        :return:
        """
        if self._length < self._capacity:
            if self._insert(self._data, num):
                self._length += 1
                return True
        return False

    @staticmethod
    def _insert(data, num):
        """
        堆中插入元素的内部实现
        :param data:
        :param num:
        :return:
        """
        assert type(data) is list
        assert type(num) is int

        data.append(num)
        length = len(data)

        # idx of New Node
        nn = length - 1
        # bottom-up
        while nn > 0:
            p = (nn-1) // 2
            if data[nn] > data[p]:
                data[nn], data[p] = data[p], data[nn]
                nn = p
            else:
                break

        return True

    def get_top(self):
        """
        取堆顶
        :return:
        """
        if self._length <= 0:
            return None
        return self._data[0]

    def remove_top(self):
        """
        取堆顶
        :return:
        """
        ret = None
        if self._length > 0:
            ret = self._remove_top(self._data)
            self._length -= 1
        return ret

    @staticmethod
    def _remove_top(data):
        """
        取堆顶内部实现
        :param data:
        :return:
        """
        assert type(data) is list

        length = len(data)
        if length == 0:
            return None

        data[0], data[-1] = data[-1], data[0]
        ret = data.pop()
        length -= 1

        # length == 0 or == 1, return
        if length > 1:
            BinaryHeap._heap_down(data, 0, length-1)

        return ret

    @staticmethod
    def _type_assert(nums):
        assert type(nums) is list
        for n in nums:
            assert type(n) is int

    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(data)

        if length == 0:
            return 'empty heap'

        ret = ''
        for i, n in enumerate(data):
            ret += str(n)
            # 每行最后一个换行
            if i == 2**int(math.log(i+1, 2)+1) - 2 or i == len(data) - 1:
                ret += '\n'
            else:
                ret += ', '

        return ret

    def __repr__(self):
        return self._draw_heap(self._data)
```


```python
nums = list(range(10))
random.shuffle(nums)

bh = BinaryHeap(nums)
print('--- before heapify ---')
print(bh)

# heapify
bh.heapify()
print('--- after heapify ---')
print(bh)

# insert
print('--- insert ---')
if bh.insert(8):
    print('insert success')
else:
    print('insert fail')
print(bh)

# get top
print('--- get top ---')
print('get top of the heap: {}'.format(bh.get_top()))
bh.remove_top()
print(bh)
```

    --- before heapify ---
    8
    7, 5
    6, 2, 1, 3
    9, 4, 0
    
    --- after heapify ---
    9
    8, 5
    7, 2, 1, 3
    6, 4, 0
    
    --- insert ---
    insert success
    9
    8, 5
    7, 8, 1, 3
    6, 4, 0, 2
    
    --- get top ---
    get top of the heap: 9
    8
    8, 5
    7, 2, 1, 3
    6, 4, 0
    
    


```python
class BinaryHeapSort(BinaryHeap):
    def __init__(self):
        super(BinaryHeap).__init__()
        
    def sort(self, nums):
        """
        排序
        1. 堆化，大顶堆
        2. 排序，从后往前遍历，首尾元素互换，子数组堆化
        :param nums:
        :return:
        """
        assert type(nums) is list
        length = len(nums)

        if length <= 1:
            return
        
        self._type_assert(nums)

        # heapify
        self._heapify(nums, length-1)

        # sort
        for i in range(length-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self._heap_down(nums, 0, i-1)

        return
```


```python
bhs = BinaryHeapSort()
nums = [3, 5, 2, 6, 1, 7, 6]

print('--- before sort ---')
print(nums)

bhs.sort(nums)
print('--- after sort ---')
print(nums)
```

    --- before sort ---
    [3, 5, 2, 6, 1, 7, 6]
    --- after sort ---
    [1, 2, 3, 5, 6, 6, 7]
    

#### 堆的应用：优先级队列
优先级队列，是一个队列。与一般的队列不同的是，在优先级队列中，数据的出队顺序不是先进先出，而是按照优先级来，优先级高的，最先出队。


```python
import math


class QueueNode:
    def __init__(self, priority, data=None):
        assert type(priority) is int and priority >= 0
        self.priority = priority
        self.data = data

    def __repr__(self):
        return str((self.priority, self.data))
```


```python
class PriorityQueue:
    def __init__(self, capacity=100):
        self._capacity = capacity
        self._q = []
        self._length = 0
        
    def enqueue(self, priority, data=None):
        if self._length >= self._capacity:
            return False
        
        new_node = QueueNode(priority, data)
        self._q.append(new_node)
        self._length += 1
        
        nn = self._length - 1
        while nn > 0:
            parent = (nn - 1) // 2
            if self._q[nn].priority < self._q[parent].priority:
                self._q[nn], self._q[parent] = self._q[parent], self._q[nn]
                nn = parent
            else:
                break
        
        return True
    
    def dequeue(self):
        if self._length <= 0:
            raise Exception('the queue is empty....')
            
        self._q[0], self._q[-1] = self._q[-1], self._q[0]
        ret = self._q.pop()
        self._length -= 1
        
        if self._length > 1:
            lp = (self._length - 2) // 2
            idx = 0
            
            while idx <= lp:
                lc = 2 * idx + 1
                rc = lc + 1
                
                if rc <= self._length - 1:
                    tmp = lc if self._q[lc].priority < self._q[rc].priority else rc
                else:
                    tmp = lc
                    
                if self._q[tmp].priority < self._q[idx].priority:
                    self._q[tmp], self._q[idx] = self._q[idx], self._q[tmp]
                    idx = tmp
                else:
                    break
        return ret
    
    def get_length(self):
        return self._length
    
    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(data)
        
        if length == 0:
            return 'empty'
        
        ret = ''
        for i, n in enumerate(data):
            ret += str(n)
            if i == 2 ** int(math.log(i + 1, 2) + 1) - 2 or i == len(data) - 1:
                ret += '\n'
            else:
                ret += ','
                
        return ret
    
    def __repr__(self):
        def formater(node):
            assert type(node) is QueueNode
            return node.priority, node.data

        data = list(map(formater, self._q))
        return self._draw_heap(data)
```


```python
pq = PriorityQueue()
pq.enqueue(5, 'Watch TV')
pq.enqueue(2, 'Learning')
pq.enqueue(10, 'Go Sleep')
pq.enqueue(0, 'Go Home')
pq.enqueue(7, 'Mobile Games')
print(pq)

while pq.get_length() > 0:
    print(pq.dequeue())
```

    (0, 'Go Home')
    (2, 'Learning'),(10, 'Go Sleep')
    (5, 'Watch TV'),(7, 'Mobile Games')
    
    (0, 'Go Home')
    (2, 'Learning')
    (5, 'Watch TV')
    (7, 'Mobile Games')
    (10, 'Go Sleep')
    

#### 利用堆求Top K


```python

```

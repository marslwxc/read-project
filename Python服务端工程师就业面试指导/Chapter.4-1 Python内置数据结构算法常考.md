
数据结构/算法 | 内置语言 | 内置库
------------- | -------- | ------
线性结构 | list/tuple | array/collections.namedtuple
链式结构 | | collections.deque(双端队列)
字典结构 | dict | collections.Counter（计数器）/OrderedDict（有序字典）
集合结构 | set/frozenset |
排序结构 | sorted |
二分算法 | | bisect模块
堆算法 | | heapq模块
缓存算法 | | functools.lru_cache(Least Tecent Used, python3)

collections模块
- namedtuple() 
- deque
- Counter
- OrderedDict
- defaultdict


```python
import collections


Point = collections.namedtuple('Point', 'x, y')
p = Point(1,2)
print(p.x, p[0], p.y, p[1])
```

    1 1 2 2
    


```python
de = collections.deque()
de.append(1)
de.append(2)
de.appendleft(0)
de.appendleft(3)
print(de, de.pop(), de.popleft())
```

    deque([0, 1]) 2 3
    


```python
c = collections.Counter("adfsafdsa")
print(c, c.most_common())
```

    Counter({'a': 3, 'd': 2, 'f': 2, 's': 2}) [('a', 3), ('d', 2), ('f', 2), ('s', 2)]
    


```python
od = collections.OrderedDict()
od['c'] = 'c'
od['a'] = 'a'
od['b'] = 'b'
print(od.keys())
```

    odict_keys(['c', 'a', 'b'])
    


```python
dd = collections.defaultdict(int)
print(dd['a'])
```

    0
    

Python dict 底层结构：使用哈希表
- 为了支持快速查找使用了哈希表作为底层结构
- 哈希表平均查找时间复杂度O(1)
- CPython解释器使用二次探查解决哈希冲突问题
- **哈希表的冲突和扩容是重要问题**

Python list/tuple区别
- 都是线性结构，支持下标访问
- list是可变对象，tuple保存的引用不可变
- list没法作为字典的key，tuple可以

LRUCache:Least-Tecently-Used 替换掉最近最少使用的对象
- 缓存提出策略，当缓存空间不够用时需要一种方式剔除key
- LRU、LFU等
- LRU通过使用一个循环双端队列不断把最新访问的key放到表头实现

LRUCache实现：
- 利用Python内置的dict+collections.OrderedDict实现
- dict用来当作k\v键值对的缓存
- OrderedDict用来实现更新最近访问的key


```python
from collections import OrderedDict


class LRUCache:
    
    def __init__(self, capacity=128):
        self.od = OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1
        
    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)
```

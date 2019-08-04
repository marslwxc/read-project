

![阻塞队列](https://static001.geekbang.org/resource/image/5e/eb/5ef3326181907dea0964f612890185eb.jpg)

**先进先出，这就是典型的队列**

队列和栈非常相似，支持的操作有限。最基本的操作也是两个：**入队**，放一个数据到队列尾部；**入队**，从队列头部取一个元素。
![栈和队列](https://static001.geekbang.org/resource/image/9e/3e/9eca53f9b557b1213c5d94b94e9dce3e.jpg)
所以，队列和栈一样，是一种**操作受限的线性数据结构**

队列可以用数组来实现，也可以用链表来实现。用数组实现的队列叫做**顺序队列**，用链表实现的队列叫做**链表队列**


```python
# 用数组来实现队列
from typing import Optional


class ArrayQueue:
    
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0
        
    def enqueue(self, item):
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self.items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True
    
    def dequeue(self):
        if self._head == self._tail:
            return None
        self._head += 1
        return self._items[self._head]
    
    def __repr__(self):
        return " ".join(item for item in self._items[self._head : self._tail])
```


```python
# 用链表实现队列
from typing import Optional

class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self._next = next
        
        
class LinkedQueue:
    
    def __init__(self):
        self._head = Optional[Node]
        self._tail = Optional[Node]
        
    def enqueue(self, value):
        new_node = Node(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node
        
    def dequeue(self):
        if self._head:
            value = self._head.data
            self._head = self._head._next
            if not self._head:
                self._tail = None
            return value
```

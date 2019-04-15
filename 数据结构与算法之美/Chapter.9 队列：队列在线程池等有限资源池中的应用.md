
当我们向固定大小的线程池中请求一个线程时，如果线程池中没有空闲资源了，这个时候线程池如何处理这个请求？是拒绝请求还是排队请求？各种处理策略又是怎么实现的呢？

# 如果理解“队列”

**先进先出**

栈只支持两种基本操作：**入栈push()和出栈pop()**

队列支持的基本操作：**入队enqueue()和出队dequeue()**

队列与站一样，也是**操作首先的线性表数据结构**。

![](https://static001.geekbang.org/resource/image/9e/3e/9eca53f9b557b1213c5d94b94e9dce3e.jpg)

# 顺序队列和链式队列

队列可以用数组来实现，也可以用链表来实现。用数组实现的队列叫做**顺序队列**，用链表实现的队列叫做**链式队列**。


```python
"""
用数组实现队列
"""
from typing import Optional

class ArrayQueue:
    
    def __init__(self, capacity:int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0
        
    def enqueue(self, item:str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self.tail = self.tail - self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True
    
    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None
        
    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head : self._tail])
```

数组实现队列需要两个指针：一个是head指针，指向对头；另一个是tail指针，指向队尾。

当a、b、c、d依次入队之后，队列中的head指针指向下标为0的位置，tail指针指向下标为4的位置
![](https://static001.geekbang.org/resource/image/5c/cb/5c0ec42eb797e8a7d48c9dbe89dc93cb.jpg)

当调用两次出队操作之后，队列中head指针指向下标为2的位置，tail指针仍然指向下标为4的位置
![](https://static001.geekbang.org/resource/image/de/0d/dea27f2c505dd8d0b6b86e262d03430d.jpg)

随着不停地进行入队出队操作，head和tail都会持续往后移动。当tail移动到最右边，即使数组中还有空闲空间，也无法继续往队列中添加数据了。

## 基于链表的队列实现方法
基于链表的实现，我们同样需要两个指针：head指针和tail指针。他们分别指向链表的第一个结点和最后一个结点。如下图所示，入队时，tail->next = new_node,tail = tail->next;出队时，head=head->next。

![](https://static001.geekbang.org/resource/image/c9/93/c916fe2212f8f543ddf539296444d393.jpg)


```python
class Node:
    
    def __init__(self, data: str, next=None):
        self.data = data
        self._next = next

class LinkedQueue:

    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
    
    def enqueue(self, value: str):
        new_node = Node(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node
    
    def dequeue(self) -> Optional[str]:
        if self._head:
            value = self._head.data
            self._head = self._head._next
            if not self._head:
                self._tail = None
            return value
    
    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current._next
        return "->".join(value for value in values)


if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)
```

    0->1->2->3->4->5->6->7->8->9
    3->4->5->6->7->8->9
    3->4->5->6->7->8->9->7->8
    

# 循环队列

![](https://static001.geekbang.org/resource/image/58/90/58ba37bb4102b87d66dffe7148b0f990.jpg)

![](https://static001.geekbang.org/resource/image/71/80/71a41effb54ccea9dd463bde1b6abe80.jpg)

可以看到，图中这个队列大小为8，开始head=4，tail=7.当有一个新的元素a入队时，放入下标为7的位置。但这个时候，并不把tail更新为8，而是将其在环中后退一位，到下标0的位置。当再有一个元素b入队时，将b放入下标为0的位置，然后tail加1更新为1。

通过这样的方法，成功避免了数据搬移操作。

在用数组实现的非循环队列中，队满的判断条件是 tail == n，队空的判断条件是 head == tail。


```python
from itertools import chain


class CircularQueue:
    
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity + 1
        self._head = 0
        self._tail = 0
        
    def enqueue(self, item:str) -> bool:
        if (self._tail + 1) % self._capacity == self._head:
            return False
        self._items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True
    
    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            item = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            return item
        
    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head : self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))
        
        
if __name__ == "__main__":
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(str(i))
    q.dequeue()
    q.dequeue()
    q.enqueue(str(5))
    print(q)
```

    2 3 4 5
    

# 阻塞队列和并发队列

阻塞队列其实就是在队列的基础上增加了阻塞操作。简单来说，就是在队列为空的时候，从队头取数据会被阻塞。因为此时还没有数据可取，知道队列中有了数据才能返回；如果队列中哥已经满了，那么插入数据的操作就会被阻塞，知道队列中有空闲位置后再插入数据，然后再返回。
![](https://static001.geekbang.org/resource/image/5e/eb/5ef3326181907dea0964f612890185eb.jpg)
![](https://static001.geekbang.org/resource/image/9f/67/9f539cc0f1edc20e7fa6559193898067.jpg)



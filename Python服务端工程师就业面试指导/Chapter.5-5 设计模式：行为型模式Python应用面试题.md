
- 迭代器模式（Iterator）：通过统一的接口迭代对象
- 观察者模式（Observer）：对象发生改变的时候，观察者执行相应动作
- 策略模式（Strategy）：针对不同规模输入使用不同的策略

迭代器模式
- Python内置对迭代器的支持
- Python里可以实现__next__和__iter__实现迭代器


```python
from collections import deque


class Stack(object):
    def __init__(self):
        self._deque = deque()
        
    def push(self, value):
        return self._deque.append(value)
    
    def pop(self):
        return self._deque.pop()
        
    def empty(self):
        return len(self._deque) == 0
    
    def __iter__(self):
        res = []
        for i in self._deque:
            res.append(i)
        for i in reversed(res):
            yield i
            

s = Stack()
s.push(1)
s.push(2)
for i in s:
    print(i)
```

    2
    1
    

观察者模式
- 发布订阅是一种最常用的实现方式
- 发布订阅用于解耦逻辑
- 可以通过回调等方式实现，当发生事件时，调用相应的回调函数

策略模式
- 根据不同的输入采用不同的策略
- 对外暴露统一的接口，内部采用不同的策略计算
- 比如买东西超过10个八折，超过20个七折


```python

```

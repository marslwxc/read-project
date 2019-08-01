
# 概念

**先进先出，后进后出**

从栈的操作特性上来看，**栈是一种“操作受限”的线性表**，只允许在一端插入和删除数据。

从功能上来说，数组或链表趋势可以替代栈。但是，特定的数据结构是对特定场景的抽象，而且，数组和链表暴露了太多的操作接口，操作上的确灵活自由，但使用时就比较不可控，自然也更容易出错

**当某个数据集合只涉及在一端插入和删除数据，并且满足后进先出，先进后出的特性，就应该首选“栈”这种数据结构**

# 如何实现一个栈

栈既可以用数组来实现，也可以用链表来实现。用数组来实现的栈叫做**顺序栈**，用链表来实现的栈叫**链式栈**


```python
"""
基于链表实现的栈
"""
from typing import Optional

class Node:
    
    def __init__(self, data: int, next=None):
        self._data = data
        self._next = next
        

class LinkedStack:
    
    def __init__(self):
        self._top: Node = None
            
    def push(self, value: int):
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top
        
    def pop(self) -> Optional[int]:
        if self._top:
            value = self._top._data
            self._top = self._top._next
            return value
    
    def __repr__(self) -> str:
        current = self._top
        nums = []
        while current:
            nums.append(current._data)
            current = current._next
        return " ".join(f"{num}" for num in nums)
    

stack = LinkedStack()
for i in range(9):
    stack.push(i)
print(stack)
for _ in range(3):
    stack.pop()
print(stack)
```

    8 7 6 5 4 3 2 1 0
    5 4 3 2 1 0
    


```python
class Stack:
    
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
```

不管是顺序栈还是链式栈，存储数据只需要大小为n的数组。**在入栈和出栈过程中，只需要一两个临时变量存储空间，所以空间复杂度是O(1)**。

# 支持动态扩容的顺序栈

如果要实现一个支持动态扩展的栈，我们只需要底层依赖一个支持动态扩容的数组就可以了。当栈满了之后，就申请一个更大的数组，将原来的数据搬移到新数组中

![](https://static001.geekbang.org/resource/image/b1/da/b193adf5db4356d8ab35a1d32142b3da.jpg)

对于出栈操作来说，操作不会涉及内存的重新申请和数据的搬移，所以**出栈的时间复杂度仍然是O(1)。但是，对于入栈操作来说，当栈中有空闲空间时，入栈操作的时间复杂度为O(1)。但当空间不够时，就需要重新申请内存和数据搬移，所以时间复杂度为O(n)。**

为了分析的方便，需要事先做一些假设和定义：
   - 占空间不够时，我们重新申请一个是原来大小两倍的数组
   - 为了简化分析，假设只有入栈操作没有出栈操作
   - 定义不涉及内存搬移的入栈操作为simple-push操作，时间复杂度为O(1)

![](https://static001.geekbang.org/resource/image/c9/bb/c936a39ad54a9fdf526e805dc18cf6bb.jpg)

**均摊时间复杂度一般都等于最好情况时间复杂度**

在大部分的情况下，入栈操作的时间复杂度O都是O(1),只有在个别时刻才会退化为O(n)，所以平均情况下的耗时接近O(1)。

# 栈在函数调用中的应用

栈作为一个比较基础的数据结构，一个比较经典的应用场景就是**函数调用栈**

操作系统给每个线程分配了一块独立的内存空间，这块内存被组织成“栈”这种结构，用来存储函数调用时的临时变量。每进入一个函数，就会将临时变量作为了一个栈帧入栈，当被调用函数执行完成，返回之后，将这个函数对应的栈帧出栈。

![](https://static001.geekbang.org/resource/image/17/1c/17b6c6711e8d60b61d65fb0df5559a1c.jpg)

# 栈在表达式求值中的应用

编译器如何利用栈来实现**表达式求值**

表达式：34+13\*9+44-12/3
求值：
    实际上，编译器就是通过两个栈来实现的。其中一个保存操作数的栈，另一个时保存运算符的栈。我们从左向右遍历表达式，当遇到数字时，就直接压入操作数栈；当遇到运算符，就与运算符栈的栈顶元素进行比较。
    
   如果比运算符栈顶元素的优先级高，就将当前运算符压入栈；如果比运算符栈顶元素的优先级低或者相同，从运算符栈中取栈顶运算符，从操作数栈的栈顶取两个操作数，然后进行计算，再把计算完的结果压入操作数栈，继续比较。
    
![运算过程](https://static001.geekbang.org/resource/image/bc/00/bc77c8d33375750f1700eb7778551600.jpg)

# 栈再括号匹配中的应用

除了用栈来实现表达式求值，还可以借助栈来检查表达式中的括号是否匹配。

假设表达式中只包含三种括号，圆括号()、方括号[]和花括号{}，并且他们可以任意嵌套。比如，{[{}]}或 [{()}([])] 等都为合法格式，而{[}()] 或 [({)] 为不合法的格式。现在给你一个包含三种括号的表达式字符串，如何检查是否合法？

可以用栈来保存为匹配的左括号，从左到右依次扫描字符串。当扫描到左括号时，则将其压入栈中；当扫描到右括号时，从栈顶取出一个左括号。如果能够匹配，则继续扫描剩下的字符串。如果扫描的过程中，遇到不能配对的右括号，或者栈中没有数据，则说明非法格式。

当所有的括号都扫描完成之后，如果栈为空，则说明字符串为合法格式；否则，说明有未匹配的左括号，为非法格式。


```python
class Solution:
    def isValid(self, s):
        '''
        type s: str
        rtype: bool
        '''
        stask = [None]
        maps = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for x in range(len(s)):
            if s[x] in maps:
                stask.append(maps[s[x]])
            elif s[x] == stask[-1]:
                stask.pop()
            else:
                return False
        return len(stask) == 1
```

# 解答标题

如何实现浏览器的前进、后退功能？

使用两个栈， X和Y。把首次浏览的页面一次压入栈X，当点击后退按钮时，再依次从栈X中出栈，并将出栈的数据依次放入栈Y。当点击前进按钮时，依次从栈Y中取出数据，放入栈X中。当栈X中没有数据时，那就说明没有页面可以继续后退浏览。当栈Y中没有数据，就说明没有页面可以点击前进按钮浏览了。

![](https://static001.geekbang.org/resource/image/4b/3d/4b579a76ea7ebfc5abae2ad6ae6a3c3d.jpg)
![](https://static001.geekbang.org/resource/image/b5/1b/b5e496e2e28fe08f0388958a0e12861b.jpg)
![](https://static001.geekbang.org/resource/image/ea/bc/ea804125bea25d25ba467a51fb98c4bc.jpg)
![](https://static001.geekbang.org/resource/image/a3/2e/a3c926fe3050d9a741f394f20430692e.jpg)


```python
class NewLinkedStack(LinkedStack):
    
    def is_empty(self):
        return not self._top
    
    
class Brower:
    
    def __init__(self):
        self.forward_stack = NewLinkedStack()
        self.back_stack = NewLinkedStack()
        
    def can_forward(self):
        if self.back_stack.is_empty():
            return False
        return True
    
    def can_back(self):
        if self.forward_stack.is_empty():
            return False
        return True
    
    def open(self, url):
        print("Open new url %s", url, end='\n')
        self.forward_stack.push(url)
        
    def back(self):
        if self.forward_stack.is_empty():
            return 
        top = self.forward_stack.pop()
        self.back_stack.push(top)
        print("back to %s" % top, end="\n")
        
    def forward(self):
        if self.back_stack.is_empty():
            return
        top = self.back_stack.pop()
        self.forward_stack.push(top)
        print("forward to %s" % top, end='\n')
        
        
if __name__ == '__main__':
    browser = Brower()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()
        
    if browser.can_forward():
        browser.forward()
        
    browser.back()
    browser.back()
    browser.back()
```

    Open new url %s a
    Open new url %s b
    Open new url %s c
    back to c
    forward to c
    back to c
    back to b
    back to a
    


```python

```

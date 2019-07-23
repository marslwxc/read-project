
栈与队列：后进先出与先进先出
- 熟练掌握用python的list或者collections.deque()实现栈与队列
- 常考题：用栈实现队列


```python
# 232. 用栈实现队列
"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。

示例:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

说明:
你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
"""
class MyQueue(object):
 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #列表（list）的功能与栈一样,stack1主要进出队列，stack2作中转
        self.stack1=[]
        self.stack2=[]
 
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        
 
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())#将stack1中的数据放入stack2中
        res=self.stack2.pop()#弹出stack2的顶元素
        while self.stack2:
            self.stack1.append(self.stack2.pop())#将stack2中的数据放入stack1中
        return res
 
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack1[0]
 
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1  


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```


```python

```

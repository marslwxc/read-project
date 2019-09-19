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
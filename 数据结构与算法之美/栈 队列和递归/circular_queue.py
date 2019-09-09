class Queue():
    def __init__(self,capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
 
    def enQueue(self,element):
        if self.full():
            print('队满')
            return
        self.queue[self.rear] = element
        self.rear  = (self.rear + 1) % self.capacity
 
    def deQueue(self):
        if self.empty():
            print('队列是空的')
            return
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        return temp
 
    def full(self):
        return (self.rear + 1) % self.capacity == self.front
 
    def empty(self):
        return self.front == self.rear
 
    def printQueue(self):
        temp = self.front
        while temp != self.rear:
            print(self.queue[temp])
            temp = (temp + 1) % self.capacity
 
    def clear(self):
        temp = self.front
        while temp != self.rear:
            self.queue[temp] = None
            temp = (temp + 1) % self.capacity
        self.rear = self.front
 
    def getHead(self):
        if self.empty():
            print('队空')
            return
        return self.queue[self.front]
 
    def length(self):
        return (self.rear - self.front + self.capacity) % self.capacity
 
if __name__ == '__main__':
    queue = Queue(10)
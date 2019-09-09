class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.font = 0
        self.tail = 0

    def length(self):
        return (self.tail - self.font + self.capacity) % self.capacity

    def full(self):
        return (self.tail - 1) % self.capacity == self.font

    def empty(self):
        return self.font == self.tail

    def enqueu(self, data):
        if self.full():return False
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity
        return True

    def dequeue(self):
        if self.empty():return False
        ret = self.queue[self.font]
        self.font = (self.font + 1) % self.capacity
        return ret
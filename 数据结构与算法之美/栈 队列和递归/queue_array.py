"""
Queue()        定义一个空队列，无参数，返回值是空队列。
enqueue(item)  在队列尾部加入一个数据项，参数是数据项，无返回值。
dequeue()      删除队列头部的数据项，不需要参数，返回值是被删除的数据，队列本身有变化。
isEmpty()      检测队列是否为空。无参数，返回布尔值。
clear()        清空队列，无参无返回值
size()         返回队列数据项的数量。无参数，返回一个整
"""
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []

    def print(self):
        print(self.queue)


if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    for i in range(5):
        q.enqueue(i)
    print(q.size())
    q.print()
    print(q.dequeue())
    q.print()
    q.clear()
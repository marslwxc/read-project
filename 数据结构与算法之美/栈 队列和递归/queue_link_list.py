"""
Queue()        定义一个空队列，无参数，返回值是空队列。
enqueue(item)  在队列尾部加入一个数据项，参数是数据项，无返回值。
dequeue()      删除队列头部的数据项，不需要参数，返回值是被删除的数据，队列本身有变化。
isEmpty()      检测队列是否为空。无参数，返回布尔值。
clear()        清空队列，无参无返回值
size()         返回队列数据项的数量。无参数，返回一个整
"""
class ListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node
class Queue:
    def __init__(self):
        self._head = None

    def enqueue(self, value):
        node = ListNode(value)
        if self._head == None:
            self._head = node
            return
        cur = self._head
        while cur._next != None:
            cur = cur._next
        cur._next = node

    def dequeue(self):
        if self._head == None:return False
        result, self._head = self._head, self._head._next
        return result.data

    def isEmpty(self):
        return self._head == None

    def clear(self):
        self._head = None

    def size(self):
        cur = self._head
        count = 0
        while cur != None:
            cur = cur._next
            count += 1
        return count


if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    for i in range(5):
        q.enqueue(i)
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
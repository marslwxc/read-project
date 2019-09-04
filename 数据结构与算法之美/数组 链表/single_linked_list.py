"""
单链表
插入 删除 查找操作
链表中存储的数据类型是Int
"""
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self._next = next_node


class SingleLinkedList:
    def __init__(self):
        self._head = None

    def find_by_value(self, data):
        p = self._head
        while p and p != data:
            p = p._next
        return p

    def find_by_index(self, index):
        p = self._head
        position = 0
        while p and index != position:
            p = p._next
        return p
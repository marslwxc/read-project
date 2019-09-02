class Node:
    def __init__(self, data, next_node):
        self.data = data
        self._next = next_node


class SingleLinkedList:
    def __init__(self):
        self._head = None
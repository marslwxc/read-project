"""

实现一个支持动态扩容的数组，初始容量为8，每次扩充2倍

Author: ZhangHanzhe
Date: 2020-01-04

"""


class Array:
    """
    一个支持动态扩容的数组
    """
    def __init__(self, capacity = None):
        """
        构造函数
        """
        if not capacity:
            self.capacity = 10
        self._data = [None] * self.capacity

    def _update(self):
        """
        动态扩容
        """
        self._data = self._data + [None] * self.capacity
        self.capacity *= 2

    def insert(self, index):
        """
        添加元素
        """
        pass
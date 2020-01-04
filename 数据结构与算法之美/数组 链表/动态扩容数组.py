# 实现一个支持动态扩容的数组，初始容量为8，每次扩充2倍

# Author: ZhangHanzhe
# Date: 2020-01-04


class Array:
    """
    一个支持动态扩容的数组
    """
    def __init__(self, capacity = None):
        """
        构造函数
        :param capacity: 数组最大容量，不指定的话默认为10
        """
        if not capacity:
            self._capacity = 10
        else:
            self._capacity = capacity
        self._size = 0
        self._data = [None] * self._capacity

    def _update(self):
        """
        动态扩容
        """
        self._data = self._data + [None] * self.capacity
        self.capacity *= 2

    def __getitem__(self, position):
        """
        使数组支持索引
        """
        return self._data[position]

    def __setitem__(self, index, value):
        """
        修改数组中的元素
        """
        self._data[index] = value

    def __iter__(self):
        """
        使数组支持迭代
        """
        for item in self._data:
            yield item

    def get_capacity(self):
        """
        返回当前数组的容量
        """
        return self._capacity

    def get_size(self):
        """
        返回当前数组中有效元素的个数
        """
        return self._size

    def is_empty(self):
        """
        判断当前数组是否为空
        """
        return self._size == 0

    def add(self, index, value):
        """
        向数组中添加一个元素
        :param index:   添加的元素所在的索引
        :param value:    所要添加的元素
        """
        if index < 0 or index > self._size:
            return False
        if self._size == self._capacity:
            self._update()
        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]
        self._data[index] = value
        self._size += 1

    def find(self, value):
        """
        在数组中查找元素，并返回元素所在的索引。
        （如果数组中存在多个elem，只返回最左边elem的索引）
        时间复杂度：O(n)
        :param value: 目标元素
        :return:     元素所在的索引，没找到则返回-1（无效值）
        """
        return self._data.index(value)

    def find_all(self, value):
        """
        找到值为elem全部元素的索引
        :param value: 目标元素
        :return:     一个列表，值为全部elem的索引
        """
        lists = []
        for i in range(self._size - 1):
            if self._data[i] == value:
                lists.append(i)
        return lists

    def remove_index(self, index):
        """
        删除索引为index的元素。index后面的元素都要向前移动一个位置
        时间复杂度：O(n)
        :param index: 目标索引
        :return:      位于该索引的元素的值
        """
        value = self._data.pop(index)
        self._size -= 1
        return value

    def remove_value(self, value):
        """
        删除数组中为value的元素。
        如果数组中不存在value，那么什么都不做。
        如果存在多个相同的value，只删除最左边的那个
        时间复杂度：O(n)
        :param value: 要删除的目标元素
        """
        self._data.remove(value)
        self._size -= 1

    def remove_all_value(self, value):
        """
        删除数组中所有值为value的元素
        :param value: 要删除的目标元素
        """
        lists = self.find_all(value)
        for i in lists:
            a = self.remove_index(i)

    def print_all(self):
        """
        对数组进行打印
        """
        for item in range(self._size):
            print(self._data[item])
"""
实现一个大小固定的有序数组，支持动态增删改查操作
"""
class Array:
    def __init__(self, capacity: int):
        self._list = []
        self.capacity = capacity

    def __len__(self):
        return len(self._list)

    def find(self, index):
        try:
            return self._list[index]
        except IndexError:
            return None

    def insert(self, index, value):
        if len(self._list) >= self.capacity:
            return False
        else:
            self._list.insert(index, value)
            return True

    def delete(self, index):
        try:
            self._list.pop(index)
            return True
        except IndexError:
            return True

    def modify(self, index, value):
        try:
            self._list[index] = value
        except Exception as e:
            return False

    def print_all(self):
        for index in self._list:
            print(index)


def test_myarray():
    array = Array(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_myarray()
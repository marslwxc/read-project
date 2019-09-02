"""
实现一个支持动态扩容的数组
"""
class Array:
    def __init__(self):
        self._list = []

    def find(self, index):
        try:
            return self._list[index]
        except IndexError:
            return None

    def insert(self, index, value):
        self._list.insert(index, value)

    def delete(self, index):
        try:
            self._list.pop(index)
            return True
        except IndexError:
            return False

    def print_all(self):
        for index in self._list:
            print(index)

def test_myarray():
    array = Array()
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_myarray()
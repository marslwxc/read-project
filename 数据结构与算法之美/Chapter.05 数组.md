
**数组(Array)是一种线性表数据结构。它用一组连续的内存空间，来存储一组具有相同类型的数据**。

**线性表**，就是数据排成像一条线一样的结构。每个线性表上的数据最多只有前和后两个方向。
![](https://static001.geekbang.org/resource/image/b6/77/b6b71ec46935130dff5c4b62cf273477.jpg)
**非线性表**，在非线性表中，数据之间的方向并不是简单的前后关系。
![](https://static001.geekbang.org/resource/image/6e/69/6ebf42641b5f98f912d36f6bf86f6569.jpg)

数组支持所及访问，根据下标随机访问的时间复杂度为O(1)

**数组插入的平均时间复杂度为O(n)。**

如果数组中存储的数据并没有任何规律，数组只是被当作一个存储数据的集合。在这种情况下，如果要将某个数组插入到k个位置，为了避免大规模的数据迁移，还有一个简单的办法，就是直接将第k位的数据搬移到数组元素的最后，把新的元素直接放入到第k个位置。利用这种处理技巧，在特定的场景下，在第k个位置插入一个元素的时间复杂度就会降为O(1)。

**如果插入数组末尾的数据，平均情况使时间复杂度为O(n)**


```python
class MyArray:
    """A simple wrapper around List.
    You cannot have -1 in the array.
    """

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def print_all(self):
        for item in self:
            print(item)
```


```python
def test_myarray():
    array = MyArray(5)
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
```

    4
    5
    3
    10
    


```python

```

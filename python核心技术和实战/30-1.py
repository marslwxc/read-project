import unittest


#将要被测试的排序函数
def sort(arr):
    l = len(arr)
    for i in range(0, l):
        for j in range(i+1, j):
            if arr[i] >= arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp


#编写子类继承 unittest.TestCase
class TestSort(unittest.TestCase):

    #以 test 开头的函数将会被测试
    def test_sort(self):
        arr = [3, 4, 1, 5, 6]
        sort(arr)
        #arrest 结果跟我们期待的一样
        self.assertEqual(arr, [1, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
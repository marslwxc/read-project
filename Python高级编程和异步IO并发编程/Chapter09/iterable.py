# 什么是迭代协议
# 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性访问数据的方式
# 下标访问方式：__getitem__;迭代器：__iter__
from collections.abc import Iterable, Iterator
a = [1, 2] 
iter_rator = iter(a)
print(isinstance(a, Iterable))
print(isinstance(a, Iterator)) 
print(isinstance(iter_rator, Iterator))
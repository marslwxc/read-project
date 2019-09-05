"""
双向链表

功能：
is_empty() 链表是否为空
length() 链表长度
travel() 遍历链表
add(item) 链表头部添加
append(item) 链表尾部添加
insert(pos, item) 指定位置添加
remove(item) 删除节点
search(item) 查找节点是否存在
"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node
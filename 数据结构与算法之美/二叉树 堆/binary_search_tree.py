"""
二叉搜索树
find,insert,delete
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BirnaySearchNode:
    def __init__(self):
        self._root = None

    def find(self, data: int):
        node = self._root
        while node and node.val != data:
            node = node.left if node.val > data else node.right
        return node

    def insert(self, data: int):
        new_node = TreeNode(data)
        if not self._root:
            self._root = new_node
            return
        parent = None
        node = self._root
        while node:
            parent = node
            node = node.left if node.val > data else node.right
        if node.val > data:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, data: int):
        node = self._root
        parent = None
        while node and node.val != data:
            parent = node
            node = node.left if node.val > data else node.right
        if not node:
            return 
        # 删除节点有两个子节点 
        if node.left and node.right:
            successor = node.right
            successor_parent = node
            while successor.left:
                successor_parent = successor.left
                successor = successor.left
            node.val = successor.val
            successor_parent.left = None
        # 删除节点为叶节点或者仅有一个节点
        child = node.left if node.left else node.right
        if not parent:
            self._root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child
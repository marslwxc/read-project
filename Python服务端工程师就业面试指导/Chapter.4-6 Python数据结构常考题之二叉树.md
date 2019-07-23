
二叉树：二叉树涉及到递归和指针操作，常结合递归考察
- 二叉树的操作很多可以用递归的方式解决，不了解递归会比较吃力
- 常考题：二叉树的镜像/反转二叉树
- 常考题：如何层序遍历二叉树（广度优先）


```python
class TreeNode:
    def __init__(self, val, left, right):
        self.val, self.left, self.right = val, left, right
```


```python
# 遍历二叉树
def pre(root):
    if root:
        print(root)
        pre(left)
        pre(right)
```


```python
# 反转二叉树
"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
```


```python
# 102. 二叉树的层次遍历
"""
给定一个二叉树，返回其按层次遍历的节点值。 
（即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
class Solution:
    def levelOrder(self, root: TreeNode):# -> List[List[int]]:
        if root is None:
            return []
        result = []
        root_nodes = [root]
        next_nodes = []
        result.append([i.val for i in root_nodes])
        while root_nodes or next_nodes:
            for node in root_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if next_nodes:
                result.append([i.val for i in next_nodes])
            root_nodes = next_nodes
            next_nodes = []
        return result
```


```python

```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        self.res = []
        self._dfs(root, 0)
        return self.res

    def _dfs(self, node, level):
        if not node:return 

        if len(self.res) < level + 1:
            self.res.append([])

        self.res[level].append(node.val)

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
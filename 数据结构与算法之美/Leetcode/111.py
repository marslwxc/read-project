# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        self.max = 0
        self.min = 0
        self._dfs(root, 1)
        return self.min
        
    def _dfs(self, node, level):
        if not node: return
        
        if not node.left and not node.right:
            if level < self.min or self.min == 0:
                self.min = level
            elif level > self.max:
                self.max = level
        
        self._dfs(node.left, level+1)
        self._dfs(node.right, level+1)
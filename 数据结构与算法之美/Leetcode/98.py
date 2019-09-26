# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        sort_list = self.sort_l(root)
        return sort_list == list(sorted(set(sort_list)))
    
    def sort_l(self, root):
        if root is None:
            return []
        return self.sort_l(root.left) + [root.val] + self.sort_l(root.right)
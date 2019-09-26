# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = collections.deque()
        queue.append(root)
        
        visited = []
        
        while queue:
            level_size = len(queue)
            level_res = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_res.append(node.val)
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
                    
            res.append(level_res)
            
        return res
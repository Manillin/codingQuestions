# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        def dfs(root, max_val):
            if not root:
                return None 
            if root.val >= max_val:
                res.append(root.val)
            dfs(root.left, max(root.val, max_val))
            dfs(root.right, max(root.val, max_val))
        
        dfs(root, float("-inf"))
        return len(res)

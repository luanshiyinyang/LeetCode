# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            depth = 1
            return self.dfs(root, depth)
        else:
            return 0
    
    def dfs(self, root, depth):
        if root.left and root.right:
            return max(self.dfs(root.left, depth), self.dfs(root.right, depth)) + 1
        if root.left:
            return self.dfs(root.left, depth) + 1
        if root.right:
            return self.dfs(root.right, depth) + 1
        return depth
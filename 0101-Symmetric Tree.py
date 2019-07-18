# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or self.bfs(root.left, root.right)
    
    def bfs(self, left, right):
        if left is None or right is None:
            return left == right
        return False if left.val != right.val else self.bfs(left.left, right.right) and self.bfs(left.right, right.left)
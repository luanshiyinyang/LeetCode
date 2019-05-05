# -*-coding:utf-8-*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pre = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        这个题目的更新思路是扫描的方式优先更新右子树（从下向上）再更新左子树（从上向下）
        """
        if root.right:
            # 优先考虑右侧
            self.bstToGst(root.right)
        root.val = self.pre = self.pre + root.val
        if root.left:
            # 当到达左侧的时候，先前走过的右侧都是pre值
            self.bstToGst(root.left)
        return root


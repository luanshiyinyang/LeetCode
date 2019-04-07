# -*-coding:utf-8-*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def search(root):
            if not root:
                return []
            res, stack = [], [(root, "")]
            while stack:
                node, ls = stack.pop()
                if not node.left and not node.right:
                    res.append(ls + str(node.val))
                if node.left:
                    stack.append((node.left, ls + str(node.val)))
                if node.right:
                    stack.append((node.right, ls + str(node.val)))
            return res
        print(search(root))




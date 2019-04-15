# -*-coding:utf-8-*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """
        说了那么多花里胡哨的，其实就是父子节点的最大插值，结合前面的题目经验，直接DFS遍历路径，对所有路径求元素差即可
        :param root:
        :return:
        """
        def search(root):
            if not root:
                return []
            res, stack = [], [(root, "")]
            while stack:
                node, ls = stack.pop()
                if not node.left and not node.right:
                    res.append(ls + "." + str(node.val))
                if node.left:
                    stack.append((node.left, ls + "." + str(node.val)))
                if node.right:
                    stack.append((node.right, ls + "." + str(node.val)))
            return res
        rst = 0
        for item in search(root):
            item = list(map(int, item.split(".")[1:]))
            item.sort()
            if len(item) > 1:
                rst = max(abs(item[len(item)-1]-item[0]), rst)
        return rst


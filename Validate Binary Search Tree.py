# -*-coding:utf-8-*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        """
        判断一个二分查找树是否合法
        核心思路，利用递归实现，传递参数small_than, large_than
        当前子树的所有值都必须小于small_than，大于large_than
        :param root:
        :return:
        """

        def search(root, small_than, large_than):
            if not root:
                # 叶子节点一定合法
                return True
            if root.val >= small_than or root.val <= large_than:
                return False
            return search(root.left, min(small_than, root.val), large_than) and search(root.right, small_than,
                                                                                       max(large_than, root.val))

        return search(root, float('inf'), float('-inf'))

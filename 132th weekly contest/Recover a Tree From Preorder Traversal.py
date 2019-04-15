# -*-coding:utf-8-*-
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        """
        其实反过来思考就是根据DFS序列生成一棵左侧优先的二叉树
        python可以利用正则表达式进行匹配
        :param S:
        :return:
        """
        import re
        tokens = re.findall(r'\d+|-+', S)
        tokens.reverse()
        tokens.append('')

        def generate(i=0):
            if tokens and len(tokens[-1]) == i:
                tokens.pop()
                node = TreeNode(int(tokens.pop()))
                node.left = generate(i + 1)
                node.right = generate(i + 1)
                return node
            else:
                return None
        return generate(i=0)

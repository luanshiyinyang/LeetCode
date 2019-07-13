# -*-coding:utf-8-*-
class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int):
        """
        中等难度的回溯题
        基本思路是合法括号只能通过下面方式生成
        "(" + generate(n-1) + ")"
        "(" + ")" + generate(n-1)
        其实如果这题是求组合数目而不是组合情况，这就是DP题目了
        left,right记录插入的左右括号数目
        :param n:
        :return:
        """

        def solve(s, left, right):
            if left == 0 and right == 0:
                self.result.append(s[:])
                return
            if left > 0:
                solve(s+"(", left-1, right)
            if left < right:
                solve(s+")", left, right-1)
        solve("", n, n)
        return self.result


print(Solution().generateParenthesis(3))


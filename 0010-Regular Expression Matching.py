# -*-coding:utf-8-*-
import re


class Solution:
    """
    由于Python内置了re模块，这题解出来并不难，但是想要理解最好还是自己设计算法
    这题的难度是hard，主要针对的解法是动态规划
    无论有没有正则表达式基础都足够理解这一题，因为这里只是正则表达式很基础的两个通配符
    "."表示匹配任意一个单字符
    "*"表示之前的元素重复若干次（包括０次）
    """

    def isMatch(self, s: str, p: str) -> bool:
        """
        方法一
        利用内置Python模块
        :param s:
        :param p:
        :return:
        """
        return re.match('^' + p + '$', s) is not None

    def isMatch2(self, s: str, p: str) -> bool:
        """
        方法二
        动态规划解法
        注意：本题可以用递归，但是一来Python实现递归有深度限制，二来递归不便于理解，这题的考点也不是递归
        动态规划和递归的区别在于动态规划拿空间换取时间
        :param s:
        :param p:
        :return:
        """
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == "*":
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)



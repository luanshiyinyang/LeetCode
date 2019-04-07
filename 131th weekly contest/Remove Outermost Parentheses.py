# -*-coding:utf-8-*-
class Solution:

    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        level = 0
        for s in S:
            if s == "(":
                if level > 0:
                    res += s
                level += 1
            else:
                level -= 1
                if level > 0:
                    res += s
        return res


Solution().removeOuterParentheses("(()())(())")

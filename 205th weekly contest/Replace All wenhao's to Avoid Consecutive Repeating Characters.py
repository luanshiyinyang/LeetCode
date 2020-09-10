class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rst, pre = "", "?"
        for i, c in enumerate(s):
            next = s[i+1] if i+1 < len(s) else "?"
            pre = c if c != "?" else {"a", "b", "c"}.difference({pre, next}).pop()
            rst += pre
        return rst

print(Solution().modifyString("??yw?ipkj?"))
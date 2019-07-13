# -*-coding:utf-8-*-
class Solution(object):
    def isMatch(self, s, p):
        """
        DP的题目用re模块做就很没意思
        给定字符串s和模式ｐ，判断能否完全匹配，可以输出True
        dp[i][j]表示s中前i个能否和p中前j个匹配
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == "" and p == "":
            return True
        if p == "":
            return False
        # 维度比原始长度大1是为了考虑dp[0][0]这样的空内容情况
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        # 首先空是可以匹配空的
        dp[0][0] = True
        # 其次，特殊情况考虑，连续的ｎ个'*'是可以匹配空的
        for i in range(1, len(dp[0])):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
        # 一般情况
        """
        若第p中第ｊ个字符是'*',
            由于'*'可以匹配空串，所以如果ｐ中前ｊ－１个字符和ｓ中前ｉ个匹配成功，返回True 即dp[i][j-1]=True则dp[i][j]=True
            由于'*'可以匹配任意字符串，若p的前ｊ个跟ｓ中的ｉ－１个匹配成功，返回True，因为ｐ中ｊ位置是'*'多加任何字符均可以　即dp[i-1][j]=True则dp[i][j]=True
        若p中第ｊ个字符不是'*',
            假设已经知道了dp[i-1][j-1]的情况，只需要判断s中的ｉ字符和ｐ中的ｊ字符，若二者相等即s[i-1]=p[j-1]或者ｐ的ｊ是'?'即p[j-1]='?'且dp[i-1][j-1]=True即为真
        """
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '?') and dp[i-1][j-1]
        return dp[len(dp)-1][len(dp[0])-1]


print(Solution().isMatch("aa", "*"))

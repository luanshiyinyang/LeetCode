class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n-2, -1, -1):
            pre = 0
            for j in range(i+1, n):
                tmp = dp[j]
                dp[j] = pre if s[i] == s[j] else 1 + min(dp[j], dp[j - 1])
                pre = tmp
        return dp[n-1]
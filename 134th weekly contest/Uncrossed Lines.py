# -*-coding:utf-8-*-
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        """
        很简单的一个DP题
        第一行的前i个数和第二行的前j个数中最大连接数目
        dp[i][j] = dp[i-1][j-1] + (A[i] == B[j]) + dp[i-1][j] + dp[i][j-1]
        """

        dp, m, n = collections.defaultdict(int), len(A), len(B)
        for i in range(m):
            for j in range(n):
                dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[m - 1, n - 1]
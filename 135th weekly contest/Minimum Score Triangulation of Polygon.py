# -*-coding:utf-8-*-
class Solution:
    def minScoreTriangulation(self, A) -> int:
        """
        直接说dp方式，在i，j之间的多边形中找到最小的k，构成i,k多边形k,j多边形以及i,j,k三角形
        注意构造dp要逆序构造
        """
        from collections import defaultdict
        dp = defaultdict(int)
        for i in range(len(A) - 2, -1, -1):
            for j in range(i + 2, len(A)):
                dp[i, j] = min([A[i] * A[j] * A[k] + dp[i, k] + dp[k, j] for k in range(i + 1, j)] or [0])
        return dp[0, len(A) - 1]


print(Solution().minScoreTriangulation([3, 7, 4, 5]))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        使用动态规划解法就是得到状态转移函数
        f(m,n)=f(m-1,n)+f(m,n-1) m>1,n>1
        f(m,n)=f(m,n-1) m=1
        f(m,n)=f(m-1,n) n=1
        f(m,n)=1 m=n=1
        :param m:
        :param n:
        :return:
        """
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                if j == 0:
                    dp[i][j] = dp[i-1][j]
                if i >0 and j>0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        def f(m, n):
            """
            设计函数递归运算,但是递归会超时
            :param m:
            :param n:
            :return:
            """
            if m == 1 and n == 1:
                return 1
            if m == 1:
                return f(m, n-1)
            if n == 1:
                return f(m-1, n)
            if m > 1 and n > 1:
                return f(m-1, n) + f(m, n-1)
        return dp[m-1][n-1]

print(Solution().uniquePaths(23, 12))
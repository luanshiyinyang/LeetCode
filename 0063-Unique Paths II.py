class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        """
        和之前那题没有障碍的类似
        注意加个障碍判断即可
        :param m:
        :param n:
        :return:
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                            dp[i][j] = 1
                    else:
                        if i == 0:
                            if obstacleGrid[i][j - 1] != 1:
                                dp[i][j] = dp[i][j-1]
                            else:
                                dp[i][j] = 0
                        if j == 0:
                            if obstacleGrid[i - 1][j] != 1:
                                dp[i][j] = dp[i-1][j]
                            else:
                                dp[i][j] = 0
                        if i > 0 and j > 0:
                            if obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1:
                                dp[i][j] = 0
                            else:
                                if obstacleGrid[i-1][j] == 1:
                                    dp[i][j] = dp[i][j-1]
                                elif obstacleGrid[i][j-1] == 1:
                                    dp[i][j] = dp[i-1][j]
                                else:
                                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

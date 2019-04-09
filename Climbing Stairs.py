# -*-coding:utf-8-*-
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        比较基础的ＤＰ题目
        对一个ｎ阶的台阶，从底到顶，一次走一步或者两步，问有多少走法
        创建一个n+1维的空间，需要多一维是因为存放到第０级，也就是原地不动有一种走法
        考虑状态方程
            dp[i]表示到第ｉ层有多少中走法
            显然到第０层和第一层只有一种走法
            对一般的ｉ，其要么是从前一层一步上来，要么是前两层两步上来即d[i]=dp[i-1]+dp[i-2]
        :param n:
        :return:
        """
        dp = [0 for i in range(n+1)]
        for i in range(n+1):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
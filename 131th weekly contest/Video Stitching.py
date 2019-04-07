# -*-coding:utf-8-*-
class Solution:
    def videoStitching(self, clips, T):
        """
        这题可以使用动态规划
        排序clips
        定义一个二维搜索空间dp[i][j]， 表示前i个clips中得到0-j秒的完整视频的最少clip的数目
        考虑边界，显然可知
        分情况考虑dp[i][j]
            如果最后一个剪辑的starttime大于等于T，那么它必然不在结果中，即dp[i][j]=dp[i-1][j]
            如果最后一个剪辑的starttime小于T，则看endtime，即dp[i][j]=min(dp[i-1][j], dp[i-1][clips[i-1][1]] +1) #加1因为选了这个clip，总数目加1
                    如果endtime大于T，取下面两个较小者
                        为了取到它，T更新为clips[i-1][0]+1；
                        不想取到它，那么忽略即可。
                    如果最后一个剪辑的endtime小于T，由于有序，不可能覆盖T了，所以设为inf
        :param clips:
        :param T:
        :return:
        """
        clips = sorted(clips, key=(lambda x: x[1]))
        dp = [[float('inf') for i in range(T+1)] for j in range(len(clips)+1)]
        for i in range(T):
            dp[0][i] = float('inf')
        for j in range(len(clips)):
            dp[j][0] = 0
        dp[0][0] = 0
        for i in range(1, len(clips)+1):
            for j in range(1, T+1):
                if clips[i-1][0] >= j:
                    dp[i][j] = dp[i-1][j]
                else:
                    if clips[i-1][1] >= j:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][clips[i-1][0]]+1)
                    else:
                        dp[i][j] = float('inf')
        return dp[len(clips)][T] if dp[len(clips)][T] < float('inf') else -1

print(Solution().videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))


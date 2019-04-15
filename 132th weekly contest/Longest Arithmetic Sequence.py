# -*-coding:utf-8-*-
class Solution:

    def longestArithSeqLength(self, A) -> int:
        """
        求有序但是不一定连续的最长公差数列的长度。
        一个二维DP，定义DP结构如下。
        DP[i][j]表示前i个数中，以j为公差的最长序列长度。
        直接考虑一般情况，若从i位置向后每一个元素与i作差，dp[j][d]要么为dp[i][d]+1要么为dp[j][d]，更新与否主要看谁大。
        注意每次更新dp时相应更新一下longest值，初始为2，因为不管怎么样起码序列有两个值。
        :param A:
        :return:
        """
        n = len(A)
        max_len = max(A) - min(A)
        dp = [[0 for i in range(2*max_len+1)] for j in range(n)]
        longest = 2
        for i in range(1, n):
            for j in range(i+1, n):
                d = A[j] - A[i]
                dp[j][d] = max((dp[i][d] + 1), dp[i][d])
                longest = max(longest, dp[i][d]+1)
        return longest
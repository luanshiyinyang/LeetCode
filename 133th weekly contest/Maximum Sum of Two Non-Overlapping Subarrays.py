class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # 暴力求解，为了方便后面的运算，预先求出l_sum[i]表示到i这个位置之前所有数的和
        l_sum = [0]
        for num in A: l_sum.append(l_sum[-1]+num)
        # i表示L最左边的指针，j表示M最左边指针
        return max(l_sum[i+L]-l_sum[i] + l_sum[j+M] - l_sum[j] for i in range(len(A) - L + 1) for j in range(len(A) - M + 1) if i>=j+M or j>=i+L)  # 此处加一是为了契合l_sum的大小
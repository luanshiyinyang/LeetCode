class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg, rst = 0, 0, 0

        for n in nums:
            if n == 0:
                pos, neg = 0, 0
                continue
            if n < 0:
                pos, neg = neg + 1 if neg > 0 else 0, pos + 1
            else:
                pos, neg = pos + 1, neg + 1 if neg > 0 else 0
            rst = max(rst, pos)
        return rst
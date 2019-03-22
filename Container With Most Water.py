# -*-coding:utf-8-*-
class Solution:
    """
    此题也有暴力解法，也就是两两计算最大值即可
    但是按照O(n)复杂度要求是选择使用贪心算法
    """
    def maxArea(self, height) -> int:
        length = len(height)
        low = 0
        high = length - 1
        maxV = 0
        while low < high:
            maxV = max(maxV, min(height[low], height[high]) * (high -low))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return maxV

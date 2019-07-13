class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = -2147483647
        cur_max = 0
        for i in range(len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            max_value = max(max_value, cur_max)

        return max_value
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        rst = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[rst] = nums[i]
                rst += 1
        return rst
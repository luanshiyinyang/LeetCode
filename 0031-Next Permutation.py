class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        partition = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                partition = i
                break
        if partition == -1:
            nums.reverse() 
        else:
            for i in range(len(nums)-1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
            nums[partition+1:len(nums)] = nums[partition+1:len(nums)][::-1]
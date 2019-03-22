# -*-coding:utf-8-*-
class Solution:
    def threeSum(self, nums):
        """
        此题目属于中等难度，要在指定的数字序列中找到三个不重复的数字且和为０，按照升序输出即可
        可以找定一个数字，然后寻找和为这个数字负数的两个数字即可
        :param nums:
        :return:
        """
        nums.sort()
        rst = []
        length = len(nums)
        for i in range(length-2):
            if i == 0 or nums[i] > nums[i-1]:
                # 此时开始向后查找
                left = i + 1
                right = length - 1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        rst.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left] + nums[right] < -nums[i]:
                        # 此时左部应该想大数方向移动
                        while left < right:
                            left += 1
                            if nums[left] > nums[left-1]:
                                break
                    else:
                        # 此时右部应该向小数方向移动
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right+1]:
                                break
        return rst

print(Solution().threeSum([-1, 4, 6,-10]))

# -*-coding:utf-8-*-
class Solution:
    def threeSumClosest(self, nums, target) -> int:
        """
        此题比起之前那一题求和为０的题目反而显得简单一点，就是个遍历求和，不断更新差值即可
        :param nums:
        :param target:
        :return:
        """
        rst = 0
        nums.sort()
        mindiff = 99999
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum - target)
                # 更新数据
                if diff < mindiff:
                    mindiff = diff
                    rst = sum
                if sum == target:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return rst


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
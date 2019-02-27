# -*-coding:utf-8-*-


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, number, target):
        dict = {}
        for i in range(len(number)):
            x = number[i]
            if target - x in dict:
                return (dict[target - x], i)
            dict[x] = i



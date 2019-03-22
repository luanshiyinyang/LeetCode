# -*-coding:utf-8-*-


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        此题比较简单，因为罗马数字不过是符号的组合，符号非常有限，而且没有乘法只有加减组合
        可以使用暴力法迅速解决这一题
        :param num:
        :return:
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        chars = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += chars[i]
        return list

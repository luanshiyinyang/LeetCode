# -*-coding:utf-8-*-


class Solution:
    """
    负数都不是回文数字
    不要将数字转化为字符串甚至字符列表，这会使用很多额外空间，也就是空间复杂度为Ｏ（１）
    注意整数溢出（Ｐｙｔｈｏｎ不需要考虑，你都溢出了，怎么可能还是回文数字
    此题又一个通用解法
    需要保证运算为整数
    """
    def isPalindrome(self, x: int) -> bool:
        # 初步判断，当ｘ是负数或者末尾数字为０，那么一定不是回文数字
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        y = 0
        while y < x:
            y = y * 10 + x % 10
            x = int(x / 10)
        return x == y or int(y / 10) == x

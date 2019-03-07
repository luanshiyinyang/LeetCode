# -*-coding:utf-8-*-
import re


class Solution:
    def myAtoi(self, s) -> int:
        '''
        注意上下界
        使用正则表达式来加快运算
        :param str:
        :return:
        '''
        s = s.strip()
        try:
            rst = re.search('(^[\+\-]?\d+)', s).group()
            rst = int(rst)
            rst = rst if rst <= 2147483647 else 2147483647
            rst = rst if rst >= -2147483648 else -2147483648
        except:
            rst = 0
        return rst


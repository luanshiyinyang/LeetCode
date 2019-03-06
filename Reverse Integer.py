# -*-coding:utf-8 -*-
class Solution:
    def reverse(self, x: 'int') -> 'int':
        maxint = 2147483649
        minint = -2147483648
        ans = int(str(abs(x))[::-1])
        return ans * (abs(x)//x) if minint < ans < maxint and ans else 0
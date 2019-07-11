class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = ((dividend < 0) == (divisor < 0))
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                res += i
                dividend -= temp
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(res, -2**31), 2**31-1)
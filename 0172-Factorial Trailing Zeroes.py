class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        find how many five
        f(n) = n/5 + f(n/5)
        """
        res = 0
        while(n>0):
            res += n // 5
            n //= 5
        return res
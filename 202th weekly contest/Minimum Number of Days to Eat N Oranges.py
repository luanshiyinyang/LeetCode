from functools import lru_cache


class Solution:
    # decorator is must
    @lru_cache()
    def minDays(self, n: int) -> int:
        # one by one is not possible, we need use dp to search by eating n % 2 one by one or n%3 one by one, then eat n/2 or 2n/3
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3)) if n > 1 else n
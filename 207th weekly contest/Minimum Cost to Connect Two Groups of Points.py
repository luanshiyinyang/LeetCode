from functools import lru_cache


class Solution:
    def connectTwoGroups(self, cost) -> int:
        m, n = len(cost), len(cost[0])
        print([x for x in zip(*cost)])
        min_arr = [min(x) for x in zip(*cost)]

        @lru_cache(None)
        def dp(i, mask):
            if i == m:
                rst = 0
                for j in range(n):
                    if not mask & (1 << j):
                        rst += min_arr[j]
                return rst

            ans = float('inf')
            for j in range(n):
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
            return ans

        return dp(0, 0)

Solution().connectTwoGroups(cost = [[15, 96], [36, 2]])
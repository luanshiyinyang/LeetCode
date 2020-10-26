from functools import lru_cache


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        presum = [0]
        for s in stoneValue:
            presum += presum[-1] + s,

        def sm(i, j):
            return presum[j + 1] - presum[i]

        @lru_cache(None)
        def helper(i, j):
            if i == j: return 0

            if all(stoneValue[k] == stoneValue[j] for k in range(i, j)):
                cnt = 0
                l = j - i + 1
                while l > 1:
                    l //= 2
                    cnt += l
                return cnt * stoneValue[j]

            res = 0
            for k in range(i, j):
                if sm(i, k) < sm(k + 1, j):
                    score = helper(i, k) + sm(i, k)
                elif sm(i, k) > sm(k + 1, j):
                    score = sm(k + 1, j) + helper(k + 1, j)
                else:
                    score = max(helper(i, k) + sm(i, k), sm(k + 1, j) + helper(k + 1, j))
                res = max(res, score)
            return res

        return helper(0, len(stoneValue) - 1)
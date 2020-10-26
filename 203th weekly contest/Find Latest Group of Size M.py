class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        if m == len(arr):
            return m
        length = [0 for i in range(len(arr) + 2)]
        res = -1
        for i, index in enumerate(arr):
            l, r = length[index-1], length[index+1]
            if l == m or r == m:
                res = i
            length[index-l] = length[index+r] = l + r + 1
        return res

print(Solution().findLatestStep(arr = [3,5,1,2,4], m = 1))
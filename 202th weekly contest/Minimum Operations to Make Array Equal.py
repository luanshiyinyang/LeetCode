class Solution:
    def minOperations(self, n: int) -> int:
        # construct arr
        arr = [2 * i + 1 for i in range(n)]
        target = sum(arr) // n
        rst = sum([target - arr[i] for i in range( n // 2)])
        return rst

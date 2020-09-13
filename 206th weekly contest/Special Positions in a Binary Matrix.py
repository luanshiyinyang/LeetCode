class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        res = 0
        row_sum = [sum(mat[i]) for i in range(m)]
        column_sum = [sum([mat[i][j] for i in range(m)]) for j in range(n)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and column_sum[j] == 1:
                    res += 1
        return res


print(Solution().numSpecial([[0, 0, 0, 0, 0],
                             [1, 0, 0, 0, 0],
                             [0, 1, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 1, 1]]))

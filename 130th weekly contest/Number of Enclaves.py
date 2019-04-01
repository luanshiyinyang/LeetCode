class Solution(object):

    def numEnclaves(self, A):
        """
        这题转化思路，从出口向内部找，不然复杂度过大
        :type A: List[List[int]]
        :rtype: int
        """
        # 出口
        outer = []
        # 总land数目
        total_ones = 0
        # 可以出去的land数目
        outer_ones = 0
        for i in range(len(A)):
            # 优先找到出口
            if i == 0 or i == len(A) - 1:
                for j in range(len(A[i])):
                    if A[i][j] == 1:
                        outer.append((i, j))
                        A[i][j] = 2
                        total_ones += 1
            else:
                for j in range(len(A[i])):
                    if A[i][j] == 1:
                        total_ones += 1
                # 找到出口
                if A[i][0] == 1:
                    A[i][0] = 2
                    outer.append((i, 0))
                if A[i][len(A[i])-1] == 1:
                    A[i][-1] = 2
                    outer.append((i, len(A[i])-1))
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while outer:
            r, c = outer.pop()
            outer_ones += 1
            for dr, dc in dirs:
                try:
                    if A[r+dr][c+dc] == 1:
                        A[r+dr][c+dc] = 2
                        outer.append((r+dr, c+dc))
                except:
                    continue
        return total_ones - outer_ones
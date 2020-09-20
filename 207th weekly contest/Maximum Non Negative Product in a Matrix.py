class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_path = [[0] * n for _ in range(m)]
        min_path = [[0] * n for _ in range(m)]
        max_path[0][0], min_path[0][0] = grid[0][0],  grid[0][0]
        # init dp array
        for j in range(1, n):
            max_path[0][j] = max_path[0][j-1] * grid[0][j]
            min_path[0][j] = min_path[0][j - 1] * grid[0][j]
        for j in range(1, m):
            max_path[j][0] = max_path[j-1][0] * grid[j][0]
            min_path[j][0] = min_path[j - 1][0] * grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                max_path[i][j] = max(max_path[i-1][j] * grid[i][j], min_path[i-1][j] * grid[i][j], max_path[i][j-1] * grid[i][j], min_path[i][j-1] * grid[i][j])
                min_path[i][j] = min(max_path[i-1][j] * grid[i][j], min_path[i-1][j] * grid[i][j], max_path[i][j-1] * grid[i][j], min_path[i][j-1] * grid[i][j])
        return max_path[-1][-1] % int(1e9 + 7) if max_path[-1][-1] >= 0 else -1
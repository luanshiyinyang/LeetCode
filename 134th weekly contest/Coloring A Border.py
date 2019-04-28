# -*-coding:utf-8-*-
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        """
        尝试使用BFS暴力遍历，只需要扫描一次即可
        核心思路还是DFS或者BFS的扫描
        注意边界不一定是棋盘边界而是颜色边缘
        """
        m, n = len(grid), len(grid[0])

        queue, visited, border = [[r0, c0]], set([(r0, c0)]), set()
        while len(queue) > 0:
            r, c = queue.pop(0)
            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r_new, c_new = r + i, c + j
                if 0 <= r_new < m and 0 <= c_new < n and grid[r_new][c_new] == grid[r][c]:
                    # 如果存在后续则不是边界
                    if (r_new, c_new) not in visited:
                        queue.append([r_new, c_new])
                        visited.add((r_new, c_new))
                else:
                    border.add((r, c))
        for x, y in border:
            grid[x][y] = color

        return grid




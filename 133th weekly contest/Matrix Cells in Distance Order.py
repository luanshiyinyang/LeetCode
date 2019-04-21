# -*-coding:utf-8-*-
from collections import deque


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        grid = [[0 for i in range(C)] for j in range(R)]
        rst = []

        def bfs(i, j, grid):
            queue = deque()
            queue.append([i, j])
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while queue:
                coor = queue.popleft()
                x, y = coor
                if grid[x][y] == 0:
                    rst.append(coor)
                    grid[x][y] = 1
                    for d in dir:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx < R and 0 <= ny < C:
                            if grid[nx][ny] == 0:
                                queue.append([nx, ny])

        bfs(r0, c0, grid)
        return rst
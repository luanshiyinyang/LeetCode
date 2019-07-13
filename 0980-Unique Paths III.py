# -*-coding:utf-8-*-
class Solution:
    def uniquePathsIII(self, grid) -> int:
        """
        不管怎么说，优先遍历比DP高效一点点
        :param grid:
        :return:
        """
        row = len(grid)
        column = len(grid[0])
        if row == 0:
            return 0
        # 方向控制参数
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.rst = 0

        def get_start(row, column, data):
            """
            得到出发位置和可走的总格子数目
            :return:
            """
            total = 0
            x, y = None, None
            for i in range(row):
                for j in range(column):
                    if data[i][j] == 0:
                        total += 1
                    if data[i][j] == 1:
                        x = i
                        y = j
            return x, y, total

        def bfs(i, j):
            """
            递归实现广度优先遍历，每次走到一个未曾访问过的位置
            :return:
            """

            if grid[i][j] == 2:
                # 走到终点，判断是否走过所有的可走位置
                if len(visited) == total:
                    self.rst += 1
            else:
                for direction in directions:
                    next_x, next_y = i + direction[0], j + direction[1]
                    # 如果下一步位置合法
                    if 0 <= next_x < row and 0 <= next_y < column:
                        pos = next_x * column + next_y
                        if pos not in visited and grid[next_x][next_y] != -1:
                            visited.add(pos)
                            bfs(next_x, next_y)
                            visited.remove(pos)

        x_start, y_start, total = get_start(row, column, grid)
        total += 2  # 需要先加上起始点和目的点
        visited = set()  # 记录访问过的结点的一维序号
        # 第一个访问的一定是起始点
        visited.add(x_start * column + y_start)
        bfs(x_start, y_start)
        return self.rst



print(Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
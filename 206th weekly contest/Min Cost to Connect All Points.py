import math


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        dis, res, curr = [math.inf] * n, 0, 0  # 随机选择一个起始点，这里选0即可
        used = set()

        # 剩余的n-1个点
        for i in range(n -1):
            x, y = points[curr]
            used.add(curr)
            for j, (x_, y_) in enumerate(points):
                if j in used:
                    continue
                dis[j] = min(dis[j], abs(x-x_) + abs(y-y_))
            min_dis, curr = min((v, idx) for idx, v in enumerate(dis))  # 得到最近的点及其编号
            res += min_dis
            dis[curr] = math.inf
        return res

print(Solution().minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))

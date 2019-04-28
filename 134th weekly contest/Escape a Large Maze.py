# -*-coding:utf-8-*-
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        看题的第一感觉是为什么又来了一道网格搜索
        原来这一题的搜索范围很大很大，很容易TLE
        但是blocked的大小最大不过200 * 200 / 2左右（19900）
        """
        blocked = set(map(tuple, blocked))
        visited = set()

        def dfs(x, y, target, step=0):
            if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in visited: return False
            visited.add((x, y))
            if step > 20000 or [x, y] == target: return True
            return dfs(x + 1, y, target, step + 1) or dfs(x - 1, y, target, step + 1) or dfs(x, y + 1, target, step + 1) or dfs(x, y - 1, target, step + 1)
        return dfs(source[0], source[1], target) and dfs(target[0], target[1], source)
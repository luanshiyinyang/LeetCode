# -*-coding:utf-8-*-
class Solution:
    def combinationSum(self, candidates, target: int):
        """
        这题是分在数组类别的一道题
        :param candidates:
        :param target:
        :return:
        """
        res = []
        candidates.sort()

        def search(candidates, target, temp):
            """
            递归搜索
            :param candidates:
            :param target:
            :param temp:
            :return:
            """
            if not target:
                res.append(temp)
                return

            for i, num in enumerate(candidates):
                if num <= target:
                    search(candidates[i:], target-num, temp + [num])
                else:
                    break

        search(candidates, target, [])
        return res


Solution().combinationSum([2, 3, 6, 7], 7)
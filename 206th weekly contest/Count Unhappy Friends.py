class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        query = {}
        res = 0
        # 这样遍历就行，因为题目限制pair中数值唯一配对
        for i, j in pairs:
            query[i] = preferences[i][:preferences[i].index(j)]
            query[j] = preferences[j][:preferences[j].index(i)]
        for i in query.keys():
            for v in query[i]:
                if i in query[v]:
                    res += 1
                    break
        return res

print(Solution().unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]))



class Solution:

    def numDupDigitsAtMostN(self, N):
        """
        这是一个排列问题，核心思路是找寻无重复的排列可能
        如：
        N = 8756
        产生L=[8, 7, 5, 7]
        结果格式
            XXX
            XX
            X
            1XXX~7XXX
            80XX~86XX
            870X~874X
            8750~8756
        :param N:
        :return:
        """
        # [8, 7, 5, 7]
        N_list = list(map(int, str(N + 1)))
        rst = 0
        # 定格式的范围
        n = len(N_list)

        def permutate(m, n):
            """
            算排列数目
            :param m:
            :param n:
            :return:
            """
            return 1 if n == 0 else permutate(m, n - 1) * (m - n + 1)

        for i in range(1, n):
            # X,XX,XXX类型的排列数目
            rst += 9 * permutate(9, i - 1)
        s = set()
        for i, x in enumerate(N_list):
            # 求剩下的形式
            for y in range(0 if i else 1, x):
                if y not in s:
                    rst += permutate(9 - i, n - i - 1)
            if x in s: break
            s.add(x)
        return N - rst


print(Solution().numDupDigitsAtMostN(8756))
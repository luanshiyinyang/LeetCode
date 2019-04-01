class Solution:

    def numPairsDivisibleBy60(self, time) -> int:
        """
        此题C++等语言可以暴力破解，Python会超时
        只要考虑对每个t，有多少x满足t+x % 60 == 0
        t % 60 + x % 60 ==0
        x = -t % 60
        注意，除了Python，其他语言需要修改这个算式
        :param time:
        :return:
        """
        rst = 0
        import collections
        count = collections.Counter()
        for item in time:
            rst += count[-item % 60]
            count[item % 60] += 1
        return rst
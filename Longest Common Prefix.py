class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        题目的意思很简单，返回一个字符串列表中多个字符串的最长共同前缀
        本题比较简单
        :param strs:
        :return:
        """
        # 特殊情况返回空字符串
        if len(strs) == 0:
            return ''
        # 若列表只有一个数据，无需匹配，返回这个字符串即可
        if len(strs) == 1:
            return strs[0]
        # 设定用于更新的最小长度，至多匹配最短的字符串长度的共同前缀
        min_len = 999999
        index = 0
        for i in range(0, len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                index = i
        # 记录最短字符串
        shortest_string = strs[index]
        list = [0 for i in range(len(shortest_string))]
        for i in range(0, len(shortest_string)):
            for j in range(0, len(strs)):
                if strs[j][i] == shortest_string[i]:
                    list[i] += 1
        Prefix = ''
        for i in range(0, len(shortest_string)):
            if list[i] == len(strs):
                Prefix += shortest_string[i]
            else:
                break
        return Prefix

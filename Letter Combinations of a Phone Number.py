class Solution:

    def letterCombinations(self, digits):
        """
        此题不用递归略有难度
        核心算法为DFS
        :param digits:
        :return:
        """
        refer_dict = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']
                      }
        if digits == "":
            return []
        if len(digits) == 1:
            return refer_dict.get(digits[0])

        def dfs(num, string, rst):
            if num == length:
                rst.append(string)
                return None
            for letter in refer_dict.get(digits[num]):
                dfs(num + 1, string + letter, rst)

        rst = []
        length = len(digits)
        dfs(0, '', rst)
        return rst


print(Solution().letterCombinations('23'))


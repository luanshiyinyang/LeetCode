# -*-coding:utf-8-*-
class Solution:
    def divisorGame(self, N: int) -> bool:
        """
        一个除数博弈题，难度既然是easy那么一定不是多么高深的，简单推导可以得到如下：
            N=1 先手必输 答案为Flase
            N=2 先手必赢 答案为True
            N=3 先手必输 答案为False
            ...
            此时可以看出奇数规律，而偶数都可以看出经过一步运算到偶数，所以先手换位，答案相反
        :param N:
        :return:
        """
        return N % 2 == 0


print(Solution().divisorGame(4))



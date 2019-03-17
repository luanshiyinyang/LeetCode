class Solution:
    def romanToInt(self, s: str) -> int:
        """
        这个题目虽然给的难度是easy，，但是个人感觉比反过来的之前那一题medium稍显复杂
        思路就是罗马数字大致是由大到小表示逐渐相加，但是也可能存在小到大的相减情况
        这里又一个简单思路：累加一直进行，但是一旦倒转输入串存在大到小的情况，虽然累加了这个数，但是再减两次这个数
        :param s:
        :return:
        """
        chars = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sum = 0
        s = s[::-1]
        last = None
        for x in s:
            if last and chars[x] < last:
                sum -= 2 * chars[x]
            sum += chars[x]
            last = chars[x]
        return sum

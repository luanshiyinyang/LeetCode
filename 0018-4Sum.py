# -*-coding:utf-8-*-
class Solution:

    def fourSum(self, num, target):
        """
        这题思路不同于3Sum，利用哈希表优化
        先对两个的和进行字典构建
        :param num:
        :param target:
        :return:
        """
        numLen, res, dict = len(num), set(), {}
        if numLen < 4:
            return []
        num.sort()
        for p in range(numLen):
            for q in range(p+1, numLen):
                if num[p]+num[q] not in dict:
                    dict[num[p]+num[q]] = [(p,  q)]
                else:
                    dict[num[p]+num[q]].append((p, q))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target-num[i]-num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j:
                            res.add((num[i], num[j], num[k[0]], num[k[1]]))
        return [list(i) for i in res]

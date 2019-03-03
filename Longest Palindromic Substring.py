# -*-coding:utf-8-*-
'''
Manacher算法:
step 1: 字符串内插入特殊字符'#'，处理后字符串长度为奇数；字符串收尾插入特殊字符，避免数组越界
step 2:逐个遍历字符，计算得到以每个字符为中心的最长回文串半径。
涉及到的变量有：存储字符i回文半径的数组P，上一个回文串的中心位置c以及回文串结束位置r。
计算字符i回文半径：本次计算尽量利用之前回文串匹配的结果，减少重复字符比对。

修改了原作者代码
'''


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        if len(s) < 2:
            return s
        T = '#'.join('@{}$'.format(s))
        n = len(T)
        P = [0]*n
        c = 0
        r = 0
        for i in range(1, n-1):
            # i关于中心c的对称位置
            i_mirror = c-(i-c)
            # 利用之前回文串字符对比重复部分
            if r > i:
                P[i] = min(r-i, P[i_mirror])
            # 中心扩展法完成之前没有涉及的字符比对
            while T[i+1+P[i]] == T[i-1-P[i]]:
                P[i] = P[i]+1
            # 更新当前回文串中心c及终止位置r
            if i+P[i] > r:
                c = i
                r = i+P[i]
        # 找到最大回文半径及对应的回文中心
        maxlen = 0
        centeridx = 0
        for i in range(1, n-1):
            if P[i] > maxlen:
                maxlen = P[i]
                centeridx = i
        # 获取最长回文串
        begin = (centeridx-maxlen)//2
        end = (centeridx+maxlen)//2
        return s[begin:end]

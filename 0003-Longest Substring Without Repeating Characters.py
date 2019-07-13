# -*-coding:utf-8-*-
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        '''
        利用两个指针和一个set同时维护
        :param s: 字符串
        :return:
        '''
        left, right = 0, 0
        result = set()
        maxLength = 0
        while left < len(s) and right < len(s):
            if s[right] in result:
                if s[left] == s[right]:
                    result.remove(s[left])
                    left += 1
                else:
                    result.remove(s[left])
                    left += 1
            else:
                result.add(s[right])
                right += 1
                maxLength = max(maxLength, len(result))

        return  maxLength

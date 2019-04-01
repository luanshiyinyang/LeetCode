class Solution(object):
    def prefixesDivBy5(self, A):
        """
        比较简单，基础题
        :type A: List[int]
        :rtype: List[bool]
        """
        A = [str(i) for i in A]
        A = "0b" + "".join(A)
        rst = []
        for i in range(2, len(A)):
            now_number = int(A[:i+1], 2)
            if now_number % 5 == 0:
                rst.append(True)
            else:
                rst.append(False)
        return rst
class Solution(object):

    def baseNeg2(self, N):
        """
        此题主要考察负进制，很多博主解释很明白了
        :type N: int
        :rtype: str
        """
        if N == 0:
            return "0"

        def mod(n, k):
            if n % k < 0:
                # 此时想办法得到同余正数
                return n-(n/k+1)*k
            else:
                return n % k
        rst = ""
        k = -2  # 进制基数
        while N:
            rst += str(mod(N, k))
            if N % k < 0:
                N = N / k + 1
            else:
                N /= k
        return rst[::-1]




print(Solution().baseNeg2(2))

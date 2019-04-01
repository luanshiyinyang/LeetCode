class Solution:

    def bitwiseComplement(self, N: int) -> int:
        """
        此题只要非负数，比较简单
        :param N:
        :return:
        """
        n = list(bin(N))
        print(n)
        for i in range(2, len(n)):
            print(n[i])
            f = lambda x: '0' if x == '1' else '1'
            n[i] = f(n[i])
        rst = ''.join(n)
        return int(rst, 2)

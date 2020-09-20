class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        idx, use = [[] for _ in range(10)], [0 for _ in range(10)]
        # 存储源字符位置
        for i, c in enumerate(s):
            idx[ord(c) - ord('0')].append(i)
        # 处理目标字符串
        for c in t:
            print(c)
            index = ord(c) - ord('0')
            # 如果使用该字符已经达到了源串中该字符的数目，那么必然失败
            if use[index] >= len(idx[index]):
                return False
            # 检查是否有更小的字符在前面
            for i in range(index):
                if use[i] < len(idx[i]) and idx[i][use[i]] < idx[index][use[index]]:
                    print("hit")
                    return False
            use[index] += 1
        return True

Solution().isTransformable(s = "12345", t = "12435")
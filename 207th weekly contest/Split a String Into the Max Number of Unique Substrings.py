class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.bt(s, seen)

    def bt(self, s, seen):
        rst = 0
        if s:
            for i in range(1, len(s)+1):
                candidate = s[:i]
                if candidate not in seen:
                    seen.add(candidate)
                    rst = max(rst, 1 + self.bt(s[i:], seen))
                    seen.remove(candidate)
        return rst


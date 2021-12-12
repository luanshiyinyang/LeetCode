class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(chr(asc | 32) if 65 <= (asc := ord(ch)) <= 90 else ch for ch in s)
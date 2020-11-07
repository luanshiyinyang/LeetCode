class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m*k > len(arr): return False
        for i in range(len(arr)-m):
            if arr[i:i+m]*k == arr[i:i+m*k]:
                return True
        return False
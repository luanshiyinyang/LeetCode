class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        return any(arr[i] % 2 + arr[i+1] % 2 + arr[i+2] % 2 == 3 for i in range(len(arr)-2))

if __name__ == '__main__':
    a = [1, 2]
    print(Solution().threeConsecutiveOdds(a))
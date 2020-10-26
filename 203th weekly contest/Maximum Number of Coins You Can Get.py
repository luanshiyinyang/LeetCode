class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)  # deascending
        value = 0
        for i in range(0, len(piles)*2 // 3, 2):
            value += piles[i+1]
        return value

# one-line
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles, reverse=True)[1:len(piles)*2//3:2])

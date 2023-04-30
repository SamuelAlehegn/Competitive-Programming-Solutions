class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        total = 0
        for i in range(1, len(piles), 2):
            if i >= 2 * len(piles) // 3:
                break
            total += piles[i]
        return total

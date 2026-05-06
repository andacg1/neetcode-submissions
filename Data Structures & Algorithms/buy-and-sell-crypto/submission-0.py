class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        maxProfit = 0
        minPrice = prices[0]
        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(minPrice, p)
        return maxProfit
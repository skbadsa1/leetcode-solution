class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        maxprofit = float('-inf')
        minstock = prices[0]
        for p in prices:
            maxprofit = max(maxprofit, p - minstock)
            minstock = min(minstock, p)
        return maxprofit
        
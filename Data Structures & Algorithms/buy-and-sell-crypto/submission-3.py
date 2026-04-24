class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for r in range(len(prices)):
            buy = prices[l] 
            profit = max(profit, prices[r] - buy)
            if prices[r] < prices[l]:
                l = r
            r+=1 
        return profit

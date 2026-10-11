class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        min_index = float('inf')
        max_profit = 0

        for i in range(n):

            min_index = min(min_index, prices[i])
            max_profit = max(max_profit, prices[i]- min_index)
        return max_profit

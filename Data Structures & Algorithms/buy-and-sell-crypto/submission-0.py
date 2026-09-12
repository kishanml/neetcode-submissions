class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        for i in range(len(prices)):

            buying_price = prices[i]
            
            for j in range(i+1,len(prices)):

                max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit
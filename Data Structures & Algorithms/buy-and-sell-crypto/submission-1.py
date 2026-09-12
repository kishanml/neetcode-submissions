class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # two - pointer
        i, j = 0,1
        n = len(prices)
        max_profit = 0

        while j < n:

            if prices[j] > prices[i]:

                max_profit = max( max_profit, prices[j] - prices[i])
            else:    
                i=j
            j+=1
        return max_profit
            

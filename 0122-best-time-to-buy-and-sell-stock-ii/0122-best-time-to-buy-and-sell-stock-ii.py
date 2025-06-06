class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)-1):
            if prices[i] < min_price:
                min_price = prices[i]
            
            profit = prices[i] - min_price

            if profit > 0 and prices[i+1] < prices[i]:
                max_profit += profit
                min_price = float('inf')

        if prices[i+1] - min_price > 0:
            max_profit += prices[i+1] - min_price

        return max_profit
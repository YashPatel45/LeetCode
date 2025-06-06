class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        min_val = float('inf')

        for val in prices:
            if val < min_val:
                min_val = val

            profit = val - min_val

            if profit > max_profit:
                max_profit = profit

            # min_val = min(min_val, val)
            # max_profit = max(max_profit, val - min_val)
            
        return max_profit

            
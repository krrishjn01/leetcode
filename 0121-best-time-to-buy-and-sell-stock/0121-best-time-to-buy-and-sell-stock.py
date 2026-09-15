class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        profit = 0

        for price in prices:
            if price < buy:
               buy = price
               sell = price
            elif price > sell:
               sell = price
               profit = max( profit, sell - buy)

        return profit

        return max_profit
        
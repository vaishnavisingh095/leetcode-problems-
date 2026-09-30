class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for j in range (len(prices)):
            if prices[j] < min_price:
                min_price = prices[j]
            else:
                profit = prices[j]-min_price
                max_profit = max(max_profit,profit)
        return max_profit

                 



        
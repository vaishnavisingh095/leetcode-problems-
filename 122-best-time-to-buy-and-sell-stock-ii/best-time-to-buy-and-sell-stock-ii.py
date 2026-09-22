class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        total_gain = 0
        day = 1

        while day < len(prices):
            if prices[day] > prices[day - 1]:
                total_gain += prices[day] - prices[day - 1]
            day += 1

        return total_gain
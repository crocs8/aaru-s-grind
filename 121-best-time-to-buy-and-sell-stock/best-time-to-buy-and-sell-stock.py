class Solution(object):
    def maxProfit(self, prices):
        sell=prices[-1]
        profit=0
        for i in range(len(prices)-2,-1,-1):
            if prices[i]>sell:
                sell=prices[i]
            else:
                profit=max(profit,sell-prices[i])
        return profit

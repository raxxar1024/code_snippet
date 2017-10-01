"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        amount_profit = 0
        for i in xrange(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                amount_profit += prices[i + 1] - prices[i]
        return amount_profit


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0

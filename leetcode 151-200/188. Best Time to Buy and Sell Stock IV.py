"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k > len(prices) / 2:
            return self.maxProfit_n(prices)
        else:
            return self.maxProfit_k(k, prices)

    def maxProfit_n(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(prices[i + 1] - prices[i], 0)
        return profit

    def maxProfit_k(self, k, prices):
        max_buy = [float("-inf") for _ in xrange(k + 1)]
        max_sell = [0 for _ in xrange(k + 1)]

        for i in xrange(len(prices)):
            for j in xrange(1, min(k, i / 2 + 1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j - 1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])

        return max_sell[k]


if __name__ == "__main__":
    assert Solution().maxProfit(2, []) == 0

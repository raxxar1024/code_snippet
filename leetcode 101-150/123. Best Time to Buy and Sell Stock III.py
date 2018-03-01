"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold_1, release_1, hold_2, release_2 = float("-inf"), 0, float("-inf"), 0
        for price in prices:
            release_2 = max(release_2, hold_2 + price)
            hold_2 = max(hold_2, release_1 - price)
            release_1 = max(release_1, hold_1 + price)
            hold_1 = max(hold_1, 0 - price)
        return release_2


if __name__ == "__main__":
    # assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert Solution().maxProfit([3, 1, 2, 8, 3, 1, 9, 6]) == 15
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0

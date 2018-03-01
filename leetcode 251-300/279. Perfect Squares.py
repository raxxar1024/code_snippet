"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""


class Solution(object):
    def numSquares_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(n + 1):
            j = 1
            while n >= i + j * j:
                dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])
                j += 1
        return dp[-1]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = [0]
        while len(num) <= n:
            num.append(min(num[-i * i] for i in range(1, int(len(num) ** 0.5 + 1))) + 1)
        return num[n]


if __name__ == "__main__":
    assert Solution().numSquares(12) == 3
    assert Solution().numSquares(13) == 2

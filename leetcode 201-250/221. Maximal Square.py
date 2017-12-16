"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        dp = [[[0, 0] for _ in xrange(len(matrix[0]) + 1)] for _ in xrange(len(matrix) + 1)]
        for i in xrange(1, len(matrix) + 1):
            for j in xrange(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j][0] = dp[i][j - 1][0] + 1
                    dp[i][j][1] = dp[i - 1][j][1] + 1

        side = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        max_square = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                side[i][j] = min(dp[i + 1][j + 1][0], dp[i + 1][j + 1][1])
                if matrix[i][j] == "1":
                    if i > 0 and j > 0:
                        side[i][j] = min(side[i][j], side[i - 1][j - 1] + 1)
                max_square = max(max_square, side[i][j] * side[i][j])

        return max_square


if __name__ == "__main__":
    assert Solution().maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]) == 4

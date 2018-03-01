"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""


class Solution(object):
    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        result = [[0 for _ in xrange(n)] for _ in xrange(m)]
        result[0][0] = grid[0][0]
        for i in xrange(1, n):
            result[0][i] = result[0][i - 1] + grid[0][i]
        for i in xrange(1, m):
            result[i][0] += result[i - 1][0] + grid[i][0]

        for i in xrange(1, m):
            for j in xrange(1, n):
                result[i][j] = min(result[i][j - 1], result[i - 1][j]) + grid[i][j]

        return result[m - 1][n - 1]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        result = [0] * n
        result[0] = grid[0][0]

        for i in xrange(1, n):
            result[i] = result[i-1]+grid[0][i]

        for i in xrange(1, len(grid)):
            result[0] += grid[i][0]
            for j in xrange(1, n):
                result[j] = min(result[j-1], result[j]) + grid[i][j]

        return result[-1]


if __name__ == "__main__":
    assert Solution().minPathSum([[1, 2], [1, 1]]) == 3
    assert Solution().minPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 21

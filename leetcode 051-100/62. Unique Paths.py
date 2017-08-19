"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

"""


class Solution(object):
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[1 for _ in xrange(n)] for _ in xrange(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                result[i][j] = result[i - 1][j] + result[i][j - 1]

        return result[m - 1][n - 1]

    def uniquePaths(self, m, n):
        result = [1] * n
        for i in xrange(1, m):
            for j in xrange(1, n):
                result[j] += result[j - 1]
        return result[n - 1]


if __name__ == "__main__":
    assert Solution().uniquePaths(99, 99) == 5716592448890534420436582360196242777068052430850904489000
    assert Solution().uniquePaths(23, 12) == 193536720
    assert Solution().uniquePaths(1, 2) == 1
    assert Solution().uniquePaths(3, 7) == 28

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def unique_path(m, n):
            if m == 1 and n == 1:
                return 1
            elif m == 1:
                return unique_path(m, n - 1)
            elif n == 1:
                return unique_path(m - 1, n)
            else:
                return unique_path(m - 1, n) + unique_path(m, n - 1)

        return unique_path(m, n)


if __name__ == "__main__":
    assert Solution().uniquePaths(23, 12) == 193536720
    assert Solution().uniquePaths(1, 2) == 1
    assert Solution().uniquePaths(3, 7) == 28

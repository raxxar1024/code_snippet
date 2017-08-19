"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[1 for _ in xrange(n)] for _ in xrange(m)]

        if obstacleGrid[0][0] == 1:
            return 0

        for i in xrange(1, n):
            if obstacleGrid[0][i] == 1:
                result[0][i] = 0
            else:
                result[0][i] = result[0][i - 1]

        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1:
                result[i][0] = 0
            else:
                result[i][0] = result[i - 1][0]

        for i in xrange(1, m):
            for j in xrange(1, n):
                result[i][j] = 0
                if obstacleGrid[i][j] == 1:
                    continue
                if obstacleGrid[i - 1][j] == 0:
                    result[i][j] += result[i - 1][j]
                if obstacleGrid[i][j - 1] == 0:
                    result[i][j] += result[i][j - 1]
        return result[m - 1][n - 1]


if __name__ == "__main__":
    assert Solution().uniquePathsWithObstacles([[0, 0], [0, 1]]) == 0
    assert Solution().uniquePathsWithObstacles([[0, 0]]) == 1
    assert Solution().uniquePathsWithObstacles([[0, 1]]) == 0
    assert Solution().uniquePathsWithObstacles([[1]]) == 0
    assert Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2

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
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        result = [1 for _ in xrange(n)]

        if obstacleGrid[0][0] == 1:
            result[0] = 0

        for i in xrange(1, n):
            if obstacleGrid[0][i] == 1:
                result[i] = 0
            else:
                result[i] = result[i - 1]

        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1:
                result[0] = 0
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    result[j] = 0
                else:
                    result[j] += result[j - 1]

        return result[n - 1]


if __name__ == "__main__":
    assert Solution().uniquePathsWithObstacles([[0, 0], [0, 1]]) == 0
    assert Solution().uniquePathsWithObstacles([[0, 0]]) == 1
    assert Solution().uniquePathsWithObstacles([[0, 1]]) == 0
    assert Solution().uniquePathsWithObstacles([[1]]) == 0
    assert Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2

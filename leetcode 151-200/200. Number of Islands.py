"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """


if __name__ == "__main__":
    grid = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0, ], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert Solution().numIslands(grid) == 1
    grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0, ], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
    assert Solution().numIslands(grid) == 3

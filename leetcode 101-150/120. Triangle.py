"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None:
            return 0
        current_level = triangle[0] + [float("inf")]
        for i in xrange(1, len(triangle)):
            next_level = [current_level[0] + triangle[i][0]]
            for j in xrange(1, len(triangle[i])):
                next_level.append(min(current_level[j - 1], current_level[j]) + triangle[i][j])
            next_level.append(float("inf"))
            current_level = next_level
        return reduce(min, current_level)


if __name__ == "__main__":
    assert Solution().minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]) == 11

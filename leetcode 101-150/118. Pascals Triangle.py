"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1]]
        for i in xrange(numRows - 1):
            next_level = [1]
            for j in xrange(len(result[-1]) - 1):
                next_level.append(result[-1][j] + result[-1][j + 1])
            next_level.append(1)
            result.append(next_level)
        return result


if __name__ == "__main__":
    assert Solution().generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

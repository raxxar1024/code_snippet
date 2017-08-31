"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        begin, end = 0, m - 1
        while begin <= end:
            middle = (begin + end) / 2
            if matrix[middle][0] < target:
                begin = middle + 1
            elif matrix[middle][0] > target:
                end = middle - 1
            else:
                return True

        row = begin - 1

        begin, end = 0, n - 1
        while begin <= end:
            middle = (begin + end) / 2
            if matrix[row][middle] < target:
                begin = middle + 1
            elif matrix[row][middle] > target:
                end = middle - 1
            else:
                return True

        return False


if __name__ == "__main__":
    assert Solution().searchMatrix([[]], 1) is False
    assert Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11) is True
    assert Solution().searchMatrix([[1]], 1) is True
    assert Solution().searchMatrix([], 0) is False
    assert Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3) is True

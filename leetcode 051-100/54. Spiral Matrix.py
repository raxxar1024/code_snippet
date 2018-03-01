"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5]

"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        result = []
        while left <= right and top <= bottom:
            for i in xrange(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            for i in xrange(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for i in reversed(xrange(left, right + 1)):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in reversed(xrange(top, bottom + 1)):
                    result.append(matrix[i][left])
                left += 1
        return result


if __name__ == "__main__":
    assert Solution().spiralOrder([]) == []
    assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

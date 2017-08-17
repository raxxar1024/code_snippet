"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top, bottom, left, right = 0, n - 1, 0, n - 1
        result = [[0 for i in xrange(n)] for i in xrange(n)]
        i = 0
        while i < n * n:
            for k in xrange(left, right + 1):
                result[top][k] = i + 1
                i += 1
            top += 1
            for k in xrange(top, bottom + 1):
                result[k][right] = i + 1
                i += 1
            right -= 1
            if i < n * n:
                for k in xrange(right, left - 1, -1):
                    result[bottom][k] = i + 1
                    i += 1
                bottom -= 1
            if i < n * n:
                for k in xrange(bottom, top - 1, -1):
                    result[k][left] = i + 1
                    i += 1
                left += 1
        return result


if __name__ == "__main__":
    assert Solution().generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

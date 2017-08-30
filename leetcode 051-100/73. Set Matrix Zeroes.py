"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)

        first_row = reduce(lambda init, i: init or matrix[0][i] == 0, xrange(m), False)
        first_column = reduce(lambda init, i: init or matrix[i][0] == 0, xrange(n), False)

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[j][i] == 0:
                    matrix[0][i], matrix[j][0] = 0, 0

        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[0][i] == 0 or matrix[j][0] == 0:
                    matrix[j][i] = 0

        if first_row:
            for i in xrange(m):
                matrix[0][i] = 0

        if first_column:
            for i in xrange(n):
                matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[0]]
    Solution().setZeroes(matrix)
    assert matrix == [[0]]

    matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    Solution().setZeroes(matrix)
    assert matrix == [[1, 0, 3], [0, 0, 0], [7, 0, 9]]

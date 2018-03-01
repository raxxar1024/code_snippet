"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6.

"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        def largestRectangleArea(heights):
            increasing, i, max_rect = [], 0, 0
            while i <= len(heights):
                if not increasing or (i < len(heights) and heights[i] > heights[increasing[-1]]):
                    increasing.append(i)
                    i += 1
                else:
                    tmp = increasing.pop()
                    if not increasing:
                        max_rect = max(max_rect, heights[tmp] * i)
                    else:
                        max_rect = max(max_rect, heights[tmp] * (i - increasing[-1] - 1))
            return max_rect

        heights = [0] * len(matrix[0])
        max_area = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area


if __name__ == "__main__":
    assert Solution().maximalRectangle(["01", "10"]) == 1
    assert Solution().maximalRectangle(["10100", "10111", "11111", "10010"]) == 6

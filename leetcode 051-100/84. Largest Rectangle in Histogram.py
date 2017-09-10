"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        increasing, max_area, i = [], 0, 0
        heights.append(0)
        while i < len(heights):
            if not increasing or heights[increasing[-1]] <= heights[i]:
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if not increasing:
                    max_area = max(max_area, heights[last] * i)
                else:
                    max_area = max(max_area, heights[last] * (i - increasing[-1] - 1))
        return max_area


if __name__ == "__main__":
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10

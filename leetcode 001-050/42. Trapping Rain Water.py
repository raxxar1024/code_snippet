"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, result = [0] * len(height), 0
        tmp = 0
        for i in xrange(len(height)):
            if tmp < height[i]:
                tmp = height[i]
            left[i] = tmp

        tmp = 0
        for i in xrange(len(height)-1, 0, -1):
            if i != len(height)-1 and min(left[i-1], tmp) > height[i]:
                result += min(left[i-1], tmp) - height[i]
            if tmp < height[i]:
                tmp = height[i]

        return result


if __name__ == "__main__":
    assert Solution().trap([]) == 0
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6

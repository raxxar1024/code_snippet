"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

"""


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """


if __name__ == "__main__":
    assert Solution().maxPoints([Point(1, 1), Point(2, 2), Point(3, 4)]) == 2

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
        length = len(points)
        if length < 3:
            return length

        ret = -1
        for i in xrange(length):
            dict_slop = {"inf": 0}
            same_point_count = 1
            for j in xrange(length):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    dict_slop["inf"] += 1
                elif points[i].x != points[j].x:
                    slop = 0.1 * (points[j].y - points[i].y) / (points[j].x - points[i].x)
                    if slop in dict_slop:
                        dict_slop[slop] += 1
                    else:
                        dict_slop[slop] = 1
                else:
                    same_point_count += 1
            ret = max(ret, max(dict_slop.values()) + same_point_count)

        return ret


if __name__ == "__main__":
    assert Solution().maxPoints([Point(0, 0), Point(94911151, 94911150), Point(94911152, 94911151)]) == 2
    assert Solution().maxPoints([Point(1, 1), Point(2, 2), Point(3, 3), Point(3, 4)]) == 3

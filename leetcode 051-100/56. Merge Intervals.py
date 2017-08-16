"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}->{}]".format(self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            current = result[-1]
            if current.end >= intervals[i].start:
                current.end = max(current.end, intervals[i].end)
            else:
                result.append(intervals[i])
        return result


if __name__ == "__main__":
    print Solution().merge([Interval(1, 4), Interval(0, 4)])
    print Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])

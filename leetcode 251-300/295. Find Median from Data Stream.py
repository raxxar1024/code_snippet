"""
Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2

Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.

"""

from heapq import heappop, heappush


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_part = []
        self.big_part = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.big_part or num > self.big_part[0]:
            heappush(self.big_part, num)
            if len(self.big_part) > len(self.small_part) + 1:
                heappush(self.small_part, -heappop(self.big_part))
        else:
            heappush(self.small_part, -num)
            if len(self.small_part) > len(self.big_part):
                heappush(self.big_part, -heappop(self.small_part))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small_part) == len(self.big_part):
            return (self.big_part[0] + (-self.small_part[0])) / 2.0
        else:
            return self.big_part[0]


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    assert obj.findMedian() == 1
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2

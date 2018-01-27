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


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.length = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.nums.append(num)
        self.nums.sort()
        self.length += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.length % 2 == 0:
            return (self.nums[self.length / 2] + self.nums[self.length / 2 - 1]) / 2.0
        else:
            return self.nums[self.length / 2]


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2

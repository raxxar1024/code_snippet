"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in xrange(rowIndex):
            result = map(lambda x, y: x + y, result + [0], [0] + result)
        return result


if __name__ == "__main__":
    assert Solution().getRow(3) == [1, 3, 3, 1]
    assert Solution().getRow(4) == [1, 4, 6, 4, 1]

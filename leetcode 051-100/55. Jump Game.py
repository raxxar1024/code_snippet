"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


if __name__ == "__main__":
    assert Solution().canJump([2, 3, 1, 1, 4]) is True
    assert Solution().canJump([3, 2, 1, 0, 4]) is False

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
        last = 0
        for i in xrange(len(nums)):
            if i > last:
                break
            last = max(last, i + nums[i])

        return last >= len(nums) - 1


if __name__ == "__main__":
    assert Solution().canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]) is True
    assert Solution().canJump([3, 2, 1]) is True
    assert Solution().canJump([2, 1, 2, 2, 1, 2, 2, 2]) is True
    assert Solution().canJump([1, 0, 1, 0]) is False
    assert Solution().canJump([0, 2, 3]) is False
    assert Solution().canJump([2, 3, 1, 1, 4]) is True
    assert Solution().canJump([3, 2, 1, 0, 4]) is False

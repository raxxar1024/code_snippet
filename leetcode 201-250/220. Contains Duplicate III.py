"""
Given an array of integers,
find out whether there are two distinct indices i and j in the array such that
the absolute difference between nums[i] and nums[j] is
at most t and the absolute difference between i and j is at most k.
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in xrange(len(nums) - 1):
            for j in xrange(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= t and j - i <= k:
                    return True
        return False


if __name__ == "__main__":
    assert Solution().containsNearbyAlmostDuplicate([-3, 3], 2, 4) is False
    assert Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1, 2], 3, 1) is True

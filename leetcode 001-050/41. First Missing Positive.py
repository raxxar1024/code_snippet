"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if len(nums) >= nums[i] > 0 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for i in xrange(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1


if __name__ == "__main__":
    assert Solution().firstMissingPositive([1, 1]) == 2
    assert Solution().firstMissingPositive([2]) == 1
    assert Solution().firstMissingPositive([1]) == 2
    assert Solution().firstMissingPositive([]) == 1
    assert Solution().firstMissingPositive([1, 2, 0]) == 3
    assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2

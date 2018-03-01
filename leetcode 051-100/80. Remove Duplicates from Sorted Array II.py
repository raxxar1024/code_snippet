"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last, same = 0, False
        for i in xrange(1, len(nums)):
            if nums[i] != nums[last] or not same:
                same = nums[i] == nums[last]
                last += 1
                nums[last] = nums[i]
        return last + 1


if __name__ == "__main__":
    assert Solution().removeDuplicates([]) == 0
    assert Solution().removeDuplicates([1]) == 1
    assert Solution().removeDuplicates([1, 1, 1, 2, 2, 3]) == 5

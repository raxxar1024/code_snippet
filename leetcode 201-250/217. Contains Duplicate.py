"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


if __name__ == "__main__":
    assert Solution().containsDuplicate([1, 2, 3]) is True
    assert Solution().containsDuplicate([1, 1, 2, 3]) is True

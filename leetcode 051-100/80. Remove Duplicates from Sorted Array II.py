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


if __name__ == "__main__":
    list_int = [1, 1, 1, 2, 2, 3]
    assert Solution().removeDuplicates(list_int) == 5
    assert list_int == [1, 1, 2, 2, 3]

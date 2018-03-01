"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

"""


class Solution(object):
    def containsDuplicate_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = {}
        for num in nums:
            if num not in num_set:
                num_set[num] = True
            else:
                return True
        return False

    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))


if __name__ == "__main__":
    assert Solution().containsDuplicate([1, 2, 3]) is False
    assert Solution().containsDuplicate([1, 1, 2, 3]) is True

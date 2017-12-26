"""
Given an integer array of size n, find all elements that appear more than |_ n/3 _| times.
The algorithm should run in linear time and in O(1) space.

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


if __name__ == "__main__":
    assert Solution().majorityElement([1, 2, 3, 4, 5]) == []
    assert Solution().majorityElement([1, 1, 3, 4, 5]) == [1]

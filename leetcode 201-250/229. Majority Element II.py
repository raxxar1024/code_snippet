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
        import collections
        return [i[0] for i in collections.Counter(nums).items() if i[1] > len(nums) / 3]


if __name__ == "__main__":
    assert Solution().majorityElement([1, 2, 3, 4, 5]) == []
    assert Solution().majorityElement([1, 1, 3, 4, 5]) == [1]

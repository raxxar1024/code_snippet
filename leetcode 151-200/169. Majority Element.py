"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than |_ n/2 _| times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


if __name__ == "__main__":
    assert Solution().majorityElement([1]) == 1
    assert Solution().majorityElement([1, 1, 2]) == 1

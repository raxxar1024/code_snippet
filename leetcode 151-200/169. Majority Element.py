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
        dict_num = {}
        max_count = 0
        max_num = 0
        for num in nums:
            if num in dict_num:
                dict_num[num] += 1
            else:
                dict_num[num] = 1
            if dict_num[num] > max_count:
                max_count = dict_num[num]
                max_num = num

        return max_num


if __name__ == "__main__":
    assert Solution().majorityElement([1]) == 1
    assert Solution().majorityElement([1, 1, 2]) == 1

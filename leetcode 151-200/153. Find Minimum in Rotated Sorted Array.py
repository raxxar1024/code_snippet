"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] <= nums[len(nums) - 1]:
            return nums[0]
        mid = len(nums) / 2
        return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))


if __name__ == "__main__":
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2, 3]) == 0

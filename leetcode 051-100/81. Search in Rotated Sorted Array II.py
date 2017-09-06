"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) / 2
            if nums[middle] == target:
                return True
            elif nums[middle] == nums[end]:
                end -= 1
            else:
                if nums[middle] < nums[end]:
                    if nums[middle] < target <= nums[end]:
                        start = middle + 1
                    else:
                        end = middle - 1
                else:
                    if nums[start] <= target < nums[middle]:
                        end = middle - 1
                    else:
                        start = middle + 1
        return False


if __name__ == "__main__":
    assert Solution().search([3, 1, 1], 3) is True
    assert Solution().search([1, 3], 3) is True
    assert Solution().search([1], 1) is True
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 5) is True

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub_sum, tmp = nums[0], 0
        for i in xrange(len(nums)):
            tmp += nums[i]
            max_sub_sum = max(tmp, max_sub_sum)
            tmp = max(tmp, 0)
        return max_sub_sum


if __name__ == "__main__":
    assert Solution().maxSubArray([-1]) == -1
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

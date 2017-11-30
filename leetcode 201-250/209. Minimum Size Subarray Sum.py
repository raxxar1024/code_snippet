"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        sum = 0
        min_len = float("inf")
        for i in xrange(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_len = min(i - start + 1, min_len)
                sum -= nums[start]
                start += 1
        return 0 if min_len == float("inf") else min_len


if __name__ == "__main__":
    assert Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3
    assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2

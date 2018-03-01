"""
Note: This is an extension of House Robber.

After robbing those houses on that street,
the thief has found himself a new place for his thievery so that he will not get too much attention.
This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(self.rob_range(0, len(nums) - 1, nums), self.rob_range(1, len(nums), nums))

    def rob_range(self, start, end, nums):
        dp = [0 for _ in xrange(end - start)]
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[start + 1])
        for i in xrange(2, end - start):
            dp[i] = max(dp[i - 2] + nums[i + start], dp[i - 1])
        return dp[-1]


if __name__ == "__main__":
    assert Solution().rob([0, 0]) == 0
    assert Solution().rob([1, 2, 3, 4]) == 6
    assert Solution().rob([1, 2, 3, 4, 5]) == 8

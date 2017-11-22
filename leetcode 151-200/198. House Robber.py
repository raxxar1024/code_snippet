"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
Also thanks to @ts for adding additional test cases.

"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp = [0 for _ in xrange(len(nums))]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]


if __name__ == "__main__":
    assert Solution().rob([1, 2, 3, 4, 5, 6, 7, 8]) == 20

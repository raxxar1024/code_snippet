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


if __name__ == "__main__":
    assert Solution().rob([1, 2, 3, 4]) == 6
    assert Solution().rob([1, 2, 3, 4, 5]) == 8

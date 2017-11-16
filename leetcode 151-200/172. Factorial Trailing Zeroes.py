"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """


if __name__ == "__main__":
    assert Solution().trailingZeroes(0) == 27
    assert Solution().trailingZeroes(17) == 2

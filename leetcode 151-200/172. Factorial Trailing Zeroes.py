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
        result = 0
        while n > 0:
            result += n / 5
            n /= 5
        return result


if __name__ == "__main__":
    assert Solution().trailingZeroes(17) == 3
    assert Solution().trailingZeroes(100) == 24

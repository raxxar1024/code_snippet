"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.

"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 0
        while m != n:
            m &= (0x7FFFFFFF << count)
            n &= (0x7FFFFFFF << count)
            count += 1
        return m


if __name__ == "__main__":
    assert Solution().rangeBitwiseAnd(5, 7) == 4

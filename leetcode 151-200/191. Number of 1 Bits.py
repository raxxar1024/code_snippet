"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""


class Solution(object):
    def hammingWeight_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count

    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count


if __name__ == "__main__":
    assert Solution().hammingWeight(11) == 3

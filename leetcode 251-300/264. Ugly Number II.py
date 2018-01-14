"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]


if __name__ == "__main__":
    assert Solution().nthUglyNumber(1) == 1
    assert Solution().nthUglyNumber(2) == 2
    assert Solution().nthUglyNumber(3) == 3
    assert Solution().nthUglyNumber(4) == 4
    assert Solution().nthUglyNumber(5) == 5
    assert Solution().nthUglyNumber(6) == 6
    assert Solution().nthUglyNumber(7) == 8
    assert Solution().nthUglyNumber(8) == 9
    assert Solution().nthUglyNumber(9) == 10
    assert Solution().nthUglyNumber(10) == 12

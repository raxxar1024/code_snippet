"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1(2) + 9(2) = 82
8(2) + 2(2) = 68
6(2) + 8(2) = 100
1(2) + 0(2) + 0(2) = 1
Credits:
Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.

"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_sum_of_squares_of_digits(tmp):
            result = 0
            for c in str(tmp):
                result += int(c)**2
            return result

        inter_result = {}
        while n != 1 and n not in inter_result:
            inter_result[n] = True
            n = get_sum_of_squares_of_digits(n)
        return n == 1


if __name__ == "__main__":
    assert Solution().isHappy(19) is True

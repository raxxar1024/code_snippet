"""
Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag = [True for _ in xrange(n)]

        for i in xrange(2, n / 2 + 1):
            if flag[i] is True:
                tmp = 2 * i
                while tmp < n:
                    flag[tmp] = False
                    tmp += i

        count = 0
        for i in xrange(2, n):
            if flag[i] is True:
                count += 1
        return count


if __name__ == "__main__":
    assert Solution().countPrimes(18) == 7

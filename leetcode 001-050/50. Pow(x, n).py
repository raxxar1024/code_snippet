"""
Implement pow(x, n).

"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        if n > 0:
            while n > 0:
                result *= x
                n -= 1
        else:
            while n < 0:
                result /= x
                n += 1
        return result


if __name__ == "__main__":
    assert Solution().myPow(8.88023, 3) == 700.28148

"""
Implement int sqrt(int x).

Compute and return the square root of x.

"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left <= right:
            mid = (left + right) / 2
            tmp = mid * mid
            if tmp > x:
                right = mid - 1
            elif tmp < x:
                left = mid + 1
            else:
                return mid
        return left - 1


if __name__ == "__main__":
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(0) == 0
    assert Solution().mySqrt(9) == 3
    assert Solution().mySqrt(8) == 2

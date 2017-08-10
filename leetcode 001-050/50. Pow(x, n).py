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
        if n < 0:
            return 1.0/self.myPow(x, -n)
        elif n == 0:
            return 1.0
        else:
            tmp = self.myPow(x, n/2)
            if n % 2 == 1:
                return tmp * tmp * x
            else:
                return tmp * tmp


if __name__ == "__main__":
    assert Solution().myPow(8.88023, 3) == 700.281482945

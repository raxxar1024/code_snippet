"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = [1, 2]
        for i in xrange(2, n):
            result.append(result[-1] + result[-2])
        return result[n - 1]


if __name__ == "__main__":
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(35) == 14930352
    assert Solution().climbStairs(3) == 3

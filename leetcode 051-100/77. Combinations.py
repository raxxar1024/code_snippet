"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.combine_rec(n, result, 0, [], k)
        return result

    def combine_rec(self, n, result, start, intermediate, k):
        if k == 0:
            result.append(intermediate[:])
        else:
            for i in xrange(start, n):
                intermediate.append(i + 1)
                self.combine_rec(n, result, i + 1, intermediate, k - 1)
                intermediate.pop()


if __name__ == "__main__":
    print Solution().combine(20, 16)
    assert Solution().combine(4, 2) == [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4], ]

"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        result, list_n, k, factor = "", [i for i in xrange(1, n + 1)], k - 1, math.factorial(n - 1)
        for i in reversed(xrange(n)):
            tmp = list_n[k / factor]
            result += str(tmp)
            list_n.remove(tmp)
            if i > 0:
                k %= factor
                factor /= i
        return result


if __name__ == "__main__":
    assert Solution().getPermutation(3, 1) == "123"
    assert Solution().getPermutation(3, 2) == "132"
    assert Solution().getPermutation(3, 3) == "213"
    assert Solution().getPermutation(3, 4) == "231"
    assert Solution().getPermutation(3, 5) == "312"
    assert Solution().getPermutation(3, 6) == "321"

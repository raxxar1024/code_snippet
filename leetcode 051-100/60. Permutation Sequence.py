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


if __name__ == "__main__":
    assert Solution().getPermutation(3, 1) == "123"
    assert Solution().getPermutation(3, 2) == "132"
    assert Solution().getPermutation(3, 3) == "213"
    assert Solution().getPermutation(3, 4) == "231"
    assert Solution().getPermutation(3, 5) == "312"
    assert Solution().getPermutation(3, 6) == "321"

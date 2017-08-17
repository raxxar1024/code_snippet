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
        list_n = [i for i in xrange(1, n + 1)]
        result = ""
        k -= 1
        while len(list_n) > 1:
            index = k / self.factorial(len(list_n) - 1)
            k %= self.factorial(len(list_n) - 1)
            result += str(list_n[index])
            del list_n[index]
        result += str(list_n[0])
        return result

    def factorial(self, n):
        return reduce(lambda x, y: x * y, xrange(1, n + 1))


if __name__ == "__main__":
    assert Solution().getPermutation(3, 1) == "123"
    assert Solution().getPermutation(3, 2) == "132"
    assert Solution().getPermutation(3, 3) == "213"
    assert Solution().getPermutation(3, 4) == "231"
    assert Solution().getPermutation(3, 5) == "312"
    assert Solution().getPermutation(3, 6) == "321"

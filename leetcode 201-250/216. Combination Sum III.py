"""
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.combination_recu(1, k, n, result, [])
        return result

    def combination_recu(self, start, k, n, result, intermediate):
        if k == 0 and n == 0:
            result.append(list(intermediate))
        if k <= 0 and n != 0:
            return
        for i in xrange(start, 10):
            intermediate.append(i)
            self.combination_recu(i + 1, k - 1, n - i, result, intermediate)
            intermediate.remove(i)


if __name__ == "__main__":
    assert Solution().combinationSum3(8, 36) == [[1, 2, 3, 4, 5, 6, 7, 8]]
    assert Solution().combinationSum3(3, 15) == [
        [1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8],
        [3, 5, 7], [4, 5, 6]
    ]
    assert Solution().combinationSum3(3, 7) == [[1, 2, 4]]
    assert Solution().combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

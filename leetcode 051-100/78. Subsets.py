"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, result, 0, [])
        return result

    def dfs(self, nums, result, start, intermediate):
        result.append(intermediate[:])
        for i in xrange(start, len(nums)):
            self.dfs(nums, result, i + 1, intermediate + [nums[i]])


if __name__ == "__main__":
    assert Solution().subsets([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

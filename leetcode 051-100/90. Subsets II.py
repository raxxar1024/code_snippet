"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        def merge(part_1, lst_part_2):
            if part_1 not in result:
                result.append(part_1)
            if not lst_part_2:
                return
            for i in xrange(len(lst_part_2)):
                tmp = part_1 + [lst_part_2[i]]
                merge(tmp, lst_part_2[i + 1:])

        merge([], nums)
        return result


if __name__ == "__main__":
    assert Solution().subsetsWithDup([1, 2, 2]) == [
        [2],
        [1],
        [1, 2, 2],
        [2, 2],
        [1, 2],
        []
    ]

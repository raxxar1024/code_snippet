"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def gen_permute(l1, l2):
            if len(l2) == 0 and l1 not in result:
                result.append(l1)
                return
            else:
                for i in xrange(len(l2)):
                    tmp1, tmp2 = list(l1), list(l2)
                    tmp1.append(tmp2[i])
                    del tmp2[i]
                    gen_permute(tmp1, tmp2)

        gen_permute([], nums)
        return result


if __name__ == "__main__":
    assert Solution().permuteUnique([1, 1, 2]) == [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]

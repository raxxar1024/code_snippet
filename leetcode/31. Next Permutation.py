class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    assert Solution().nextPermutation([1, 2, 3]) == [1, 3, 2]
    assert Solution().nextPermutation([3, 2, 1]) == [1, 2, 3]
    assert Solution().nextPermutation([1, 1, 5]) == [1, 5, 1]


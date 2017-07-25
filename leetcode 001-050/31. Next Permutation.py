class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                k = i
                break

        if k == -1:
            nums.reverse()
            return

        for i in xrange(len(nums)-1, k, -1):
            if nums[i] > nums[k]:
                break

        nums[k], nums[i] = nums[i], nums[k]
        nums[k+1:] = nums[k+1:][::-1]


if __name__ == "__main__":
    nums = [5, 1, 1]
    Solution().nextPermutation(nums)
    assert nums == [1, 1, 5]

    nums = [1, 1]
    Solution().nextPermutation(nums)
    assert nums == [1, 1]

    nums = [1, 5, 1]
    Solution().nextPermutation(nums)
    assert nums == [5, 1, 1]

    nums = [1, 3, 2]
    Solution().nextPermutation(nums)
    assert nums == [2, 1, 3]

    nums = [1, 2]
    Solution().nextPermutation(nums)
    assert nums == [2, 1]

    nums = [1]
    Solution().nextPermutation(nums)
    assert nums == [1]

    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    assert nums == [1, 3, 2]

    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    assert nums == [1, 2, 3]

    nums = [1, 1, 5]
    Solution().nextPermutation(nums)
    assert nums == [1, 5, 1]


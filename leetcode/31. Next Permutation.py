class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        if i == -1:
            return

        while nums[i] >= nums[i+1]:
            i -= 1
            if i == -1:
                nums.reverse()
                return

        j = len(nums)-1
        while nums[i] >= nums[j] and j >= 0:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[:i:-1]
        return


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


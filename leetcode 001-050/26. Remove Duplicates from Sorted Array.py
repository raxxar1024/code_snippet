class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        tmp, i = nums[0]-1, 0
        while i < len(nums):
            if nums[i] == tmp:
                del nums[i]
            else:
                tmp = nums[i]
                i += 1

        return len(nums)

if __name__ == "__main__":
    assert Solution().removeDuplicates([1, 1, 2]) == 2




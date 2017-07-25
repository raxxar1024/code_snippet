class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_1, val_1 in enumerate(nums):
            nums_copy = nums[:]
            nums_copy.remove(val_1)
            if (target-val_1) in nums_copy:
                for index_2, val_2 in enumerate(nums_copy):
                    if val_2 == target-val_1:
                        return [index_1, index_2+1]

if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    s = Solution()
    s.twoSum(nums, target)


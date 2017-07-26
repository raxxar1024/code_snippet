class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)/2
            if target == nums[m]:
                return m
            else:
                if nums[m] < nums[r]:
                    if nums[m] < target <= nums[r]:
                        l = m+1
                    else:
                        r = m-1
                else:
                    if nums[0] <= target < nums[m]:
                        r = m-1
                    else:
                        l = m+1
        return -1


if __name__ == "__main__":
    assert Solution().search([1, 3], 3) == 1
    assert Solution().search([1], 0) == -1
    assert Solution().search([1], 1) == 0
    assert Solution().search([4, 5, 1, 2, 3], 2) == 3
    assert Solution().search([4, 5, 1, 2, 3], 1) == 2
    assert Solution().search([4, 5, 1, 2, 3], 0) == -1
    assert Solution().search([], 5) == -1


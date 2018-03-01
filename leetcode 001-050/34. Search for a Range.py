class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = self.search(lambda x, y: x >= y, nums, target)
        if l > len(nums)-1 or nums[l] != target:
            return [-1, -1]
        r = self.search(lambda x, y: x > y, nums, target)
        return [l, r-1]

    def search(self, compare, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)/2
            if compare(nums[m], target):
                r = m - 1
            else:
                l = m + 1
        return l


if __name__ == "__main__":
    assert Solution().searchRange([1], 0) == [-1, -1]
    assert Solution().searchRange([5, 7, 8, 8, 8, 10, 11], 8) == [2, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10, 11], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 11) == [-1, -1]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except ValueError:
            return -1


if __name__ == "__main__":
    assert Solution().search([4, 5, 1, 2, 3], 1) == 2
    assert Solution().search([4, 5, 1, 2, 3], 0) == -1


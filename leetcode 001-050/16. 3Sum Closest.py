class Solution(object):
    def threeSumClosest(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_val = nums[0] + nums[1] + nums[2]

        for i in xrange(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                if abs(tmp_sum - target) < abs(closest_val - target):
                    closest_val = tmp_sum
                if tmp_sum - target > 0:
                    k -= 1
                else:
                    j += 1

        return closest_val


if __name__ == "__main__":
    assert Solution().threeSumClosest([1, 2, 5, 10, 11], 12) == 13
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert Solution().threeSumClosest([0, 2, 1, -3], 1) == 0



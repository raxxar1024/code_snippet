"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""


class Solution(object):
    def longestConsecutive_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 0:
            return 0
        prev, max_len, tmp_len = nums[0], 1, 1
        for i in xrange(1, len(nums)):
            if nums[i] == prev + 1:
                tmp_len += 1
                prev = nums[i]
            else:
                tmp_len = 1
                prev = nums[i]
            max_len = max(max_len, tmp_len)
        return max_len

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        result, lengths = 1, {key: 0 for key in nums}
        for i in nums:
            if lengths[i] == 0:
                lengths[i] = 1
                left, right = lengths.get(i - 1, 0), lengths.get(i + 1, 0)
                length = 1 + left + right
                result, lengths[i - left], lengths[i + right] = max(result, length), length, length
        return result
    

if __name__ == "__main__":
    assert Solution().longestConsecutive([1, 2, 0, 1]) == 3
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4

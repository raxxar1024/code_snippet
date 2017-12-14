"""
Given an array of integers,
find out whether there are two distinct indices i and j in the array such that
the absolute difference between nums[i] and nums[j] is
at most t and the absolute difference between i and j is at most k.
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
        import collections
        num_dicts = collections.OrderedDict()

        for num in nums:
            bucket = num // max(1, t)
            for m in (bucket - 1, bucket, bucket + 1):
                if m in num_dicts and abs(num - num_dicts[m]) <= t:
                    return True
            num_dicts[bucket] = num
            if len(num_dicts) > k:
                num_dicts.popitem(False)

        return False


if __name__ == "__main__":
    assert Solution().containsNearbyAlmostDuplicate([-1, -1], 1, 0) is True
    assert Solution().containsNearbyAlmostDuplicate([-3, 3], 2, 4) is False
    assert Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1, 2], 3, 1) is True

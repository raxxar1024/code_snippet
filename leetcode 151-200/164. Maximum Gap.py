"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

Credits:
Special thanks to @porker2008 for adding this problem and creating all test cases.

"""


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        gap = max(1, (max_val - min_val) / (len(nums) - 1))
        bucket_size = (max_val - min_val) / gap + 1
        buckets = [{"min": float("inf"), "max": float("-inf")} for _ in xrange(bucket_size)]

        for n in nums:
            if n in [max_val, min_val]:
                continue
            i = (n - min_val) / gap
            buckets[i]["min"] = min(buckets[i]["min"], n)
            buckets[i]["max"] = max(buckets[i]["max"], n)

        max_gap, pre_bucket_max = 0, min_val
        for i in xrange(bucket_size):
            if buckets[i]["min"] == float("inf") and buckets[i]["max"] == float("-inf"):
                continue
            max_gap = max(max_gap, buckets[i]["min"] - pre_bucket_max)
            pre_bucket_max = buckets[i]["max"]

        max_gap = max(max_gap, max_val - pre_bucket_max)

        return max_gap


if __name__ == "__main__":
    assert Solution().maximumGap([3, 2, 3, 1, 2, 3]) == 1

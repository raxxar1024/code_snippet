"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 <= k <= array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

"""


class Solution(object):
    def findKthLargest_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest(self, nums, k):
        import random
        pivot = random.choice(nums)
        nums_1, nums_2 = [], []
        for num in nums:
            if num > pivot:
                nums_1.append(num)
            elif num < pivot:
                nums_2.append(num)
        if k <= len(nums_1):
            return self.findKthLargest(nums_1, k)
        if k > (len(nums) - len(nums_2)):
            return self.findKthLargest(nums_2, k - (len(nums) - len(nums_2)))
        return pivot


if __name__ == "__main__":
    assert Solution().findKthLargest([99, 99], 1) == 99
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5

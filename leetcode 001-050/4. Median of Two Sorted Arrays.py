class Solution(object):
    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 == 1:
            return nums[len(nums)/2]
        else:
            return (nums[len(nums)/2-1] + nums[len(nums)/2]) / 2.0

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKth(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        idx_1 = min(len(nums1), k/2)
        idx_2 = min(len(nums2), k/2)
        if nums1[idx_1-1] > nums2[idx_2-1]:
            return self.findKth(nums1, nums2[idx_2:], k-idx_2)
        else:
            return self.findKth(nums1[idx_1:], nums2, k-idx_1)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_sum = len(nums1)+len(nums2)
        if len_sum%2 == 1:
            return self.findKth(nums1, nums2, len_sum/2+1)
        else:
            return (self.findKth(nums1, nums2, len_sum/2) + self.findKth(nums1, nums2, len_sum/2+1))/2.0


if __name__ == "__main__":
    nums1, nums2 = [1, 3], [2]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.0
    # assert Solution().findKth(nums1, nums2, 3) == 3.0
    nums1, nums2 = [1, 2], [3, 4]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5


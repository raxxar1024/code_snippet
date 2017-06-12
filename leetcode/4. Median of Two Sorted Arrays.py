class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


if __name__ == "__main__":
    nums1, nums2 = [1, 3], [2]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.0
    nums1, nums2 = [1, 2], [3, 4]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 2.5


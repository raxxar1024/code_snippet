"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.

"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 or j >= 0:
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
                continue
            if j < 0:
                break
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == "__main__":
    num1, m, num2, n = [0], 0, [1], 1
    Solution().merge(num1, m, num2, n)
    assert num1 == [1]

    num1, m, num2, n = [1, 3, 5, 0, 0, 0, 0], 3, [2, 4, 6], 3
    Solution().merge(num1, m, num2, n)
    assert num1 == [1, 2, 3, 4, 5, 6, 0]

    num1, m, num2, n = [1], 1, [], 0
    Solution().merge(num1, m, num2, n)
    assert num1 == [1]

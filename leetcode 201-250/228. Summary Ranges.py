"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        start = nums[0]
        result = []
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue
            else:
                if nums[i - 1] == start:
                    result.append(str(start))
                else:
                    result.append("%d->%d" % (start, nums[i - 1]))
                start = nums[i]

        if nums[-1] == start:
            result.append(str(start))
        else:
            result.append("%d->%d" % (start, nums[-1]))
        return result


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]

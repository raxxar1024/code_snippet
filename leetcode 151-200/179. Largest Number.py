"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(n) for n in nums]
        nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
        result = "".join(nums)
        return result.lstrip("0") or "0"


if __name__ == "__main__":
    assert Solution().largestNumber([0, 0]) == "0"
    assert Solution().largestNumber([3, 30, 34, 5, 9]) == "9534330"

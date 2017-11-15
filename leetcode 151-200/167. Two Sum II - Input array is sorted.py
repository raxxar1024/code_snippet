"""
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""


class Solution(object):
    def twoSum_2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        import collections

        dict_nums = collections.defaultdict(list)
        for i in xrange(len(numbers)):
            dict_nums[numbers[i]].append(i + 1)

        for num in numbers:
            if num * 2 == target and len(dict_nums[num]) >= 2:
                return [dict_nums[num][0], dict_nums[num][1]]
            if target - num in dict_nums:
                return [dict_nums[num][0], dict_nums[target - num][0]]

        return []

    def twoSum(self, numbers, target):
        start, end = 0, len(numbers) - 1

        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]


if __name__ == "__main__":
    assert Solution().twoSum([0, 0, 3, 4], 0) == [1, 2]
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]

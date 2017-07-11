class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import collections
        result, hash_table, nums = [], collections.defaultdict(list), sorted(nums)
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                hash_table[nums[i]+nums[j]].append([i, j])

        for k in hash_table:
            if target-k in hash_table:
                for item_1 in hash_table[k]:
                    for item_2 in hash_table[target-k]:
                        [a, b], [c, d] = item_1, item_2
                        if a is not c and a is not d and b is not c and b is not d:
                            tmp = sorted(nums[a], nums[b], nums[c], nums[d])
                            if tmp not in result:
                                result.append(tmp)

        return result

if __name__ == "__main__":
    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]

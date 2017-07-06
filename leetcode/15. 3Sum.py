class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret_nums_array = []
        for index, num in enumerate(nums):
            # print index, num
            nums_copy = nums[:]
            nums_copy.remove(nums[index])
            ret_2_nums = self.find_2_num(nums_copy, -1*num)
            for ret_2_num in ret_2_nums:
                tmp = [num] + ret_2_num
                tmp.sort()
                ret_nums_array.append(tmp)

        ret_nums2 = []
        for ret_nums in ret_nums_array:
            if ret_nums not in ret_nums2:
                ret_nums2.append(ret_nums)

        return ret_nums2

    def find_2_num(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return List[List[int]]
        """
        tmp = []
        for index_1, num_1 in enumerate(nums):
            nums_copy = nums[:]
            nums_copy.remove(nums[index_1])
            for index_2, num_2 in enumerate(nums_copy):
                if num_2 == target - num_1:
                    tmp.append([num_1, num_2])
        return tmp


if __name__ == "__main__":
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]

    assert Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) == [[-4, -2, 6], [-4, 0, 4],
                                                                                      [-4, 1, 3], [-4, 2, 2],
                                                                                      [-2, -2, 4], [-2, 0, 2]]


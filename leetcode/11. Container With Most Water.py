class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max_area = 0
        # for i in xrange(len(height)):
        #     for j in xrange(len(height)):
        #         tmp_area = min(height[i], height[j]) * abs(i-j)
        #         if max_area < tmp_area:
        #             max_area = tmp_area
        # return max_area
        max_val, i, j = 0, 0, len(height)-1
        while i < j:
            tmp = min(height[i], height[j]) * (j-i)
            if tmp > max_val:
                max_val = tmp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_val


if __name__ == "__main__":
    assert Solution().maxArea([1, 2, 3]) is 2
    assert Solution().maxArea([1, 2, 3, 3]) is 4


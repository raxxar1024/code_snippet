class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


if __name__ == "__main__":
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [
        [7],
        [2, 2, 3]
    ]

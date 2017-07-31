class Solution(object):
	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""


if __name__ == "__main__":
	assert Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]

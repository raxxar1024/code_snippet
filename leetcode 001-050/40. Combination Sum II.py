class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.combinationSum2Recu(sorted(candidates), result, 0, [], target)
        return result

    def combinationSum2Recu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        prev = 0
        while start < len(candidates) and target >= candidates[start]:
            if prev != candidates[start]:
                intermediate.append(candidates[start])
                self.combinationSum2Recu(candidates, result, start+1, intermediate, target-candidates[start])
                intermediate.pop()
                prev = candidates[start]
            start += 1

if __name__ == "__main__":
    assert Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

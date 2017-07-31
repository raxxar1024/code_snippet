class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def find_result(l):
            tmp = sum(l)
            if tmp == target:
                tmp_l = list(l)
                tmp_l.sort()
                if tmp_l not in results:
                    results.append(tmp_l)
                return True
            elif tmp > target:
                return False
            else:
                for i in candidates:
                    l.append(i)
                    if find_result(l) is False:
                        l.pop()
                        break
                    l.pop()
                return True
        candidates.sort()
        results = []
        find_result([])
        return results

    def combinationSum(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), 0, result, [], target)
        return result

    def combinationSumRecu(self, candidates, start, result, intermediate, target):
        if target == 0:
            result.append(list(intermediate))
        while start < len(candidates) and candidates[start] <= target:
            intermediate.append(candidates[start])
            self.combinationSumRecu(candidates, start, result, intermediate, target-candidates[start])
            intermediate.pop()
            start += 1


if __name__ == "__main__":
    assert Solution().combinationSum([8, 7, 4, 3], 11) == [[3, 4, 4], [3, 8], [4, 7]]
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum([1, 2], 4) == [[1, 1, 1, 1], [1, 1, 2], [2, 2]]

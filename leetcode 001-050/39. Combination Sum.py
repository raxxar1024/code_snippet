class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from copy import deepcopy

        def find_result(l):
            tmp = sum(l)
            if tmp == target:
                tmp_l = deepcopy(l)
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


if __name__ == "__main__":
    assert Solution().combinationSum([8, 7, 4, 3], 11) == [[3, 4, 4], [3, 8], [4, 7]]
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum([1, 2], 4) == [[1, 1, 1, 1], [1, 1, 2], [2, 2]]

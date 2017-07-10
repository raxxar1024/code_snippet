class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        dict_nums = {"0": " ", "1": "*", "2": "abc", "3": "def", "4": "ghi",
                     "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        len_digits = len(digits)

        def dfs(idx, tmp_str, result):
            if idx == len_digits:
                result.append(tmp_str)
            else:
                for item in dict_nums[digits[idx]]:
                    dfs(idx+1, tmp_str+item, result)

        dfs(0, "", result)
        return result


if __name__ == "__main__":
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert Solution().letterCombinations("10") == ["* "]
    assert Solution().letterCombinations("12") == ["*a", "*b", "*c"]
    assert Solution().letterCombinations("") == []




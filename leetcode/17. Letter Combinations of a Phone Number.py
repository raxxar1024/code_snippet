class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """


if __name__ == "__main__":
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert Solution().letterCombinations("10") == ["* "]
    assert Solution().letterCombinations("12") == ["*a", "*b", "*c"]
    assert Solution().letterCombinations("") == []




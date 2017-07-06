class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """


if __name__ == "__main__":
    assert Solution().longestCommonPrefix([]) == ""
    assert Solution().longestCommonPrefix(["123", "1", "122"]) == "1"
    assert Solution().longestCommonPrefix(["123", "1", "q22"]) == ""
    assert Solution().longestCommonPrefix(["123"]) == "123"

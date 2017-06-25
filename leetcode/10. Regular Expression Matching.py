class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """


if __name__ == "__main__":
    assert Solution().isMatch("aa","a") == False
    assert Solution().isMatch("aa","aa") == True
    assert Solution().isMatch("aaa","aa") == False
    assert Solution().isMatch("aa","a*") == True
    assert Solution().isMatch("aa", ".*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

if __name__ == "__main__":
    s = "babad"
    assert Solution().longestPalindrome(s) == "bab"
    s = "cbbd"
    assert Solution().longestPalindrome(s) == "bb"
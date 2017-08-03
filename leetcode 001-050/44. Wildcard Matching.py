"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "*") ? true
isMatch("aa", "a*") ? true
isMatch("ab", "?*") ? true
isMatch("aab", "c*a*b") ? false

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """


if __name__ == "__main__":
    assert Solution().isMatch("aa", "a") is False
    assert Solution().isMatch("aa", "aa") is True
    assert Solution().isMatch("aaa", "aa") is False
    assert Solution().isMatch("aa", "*") is True
    assert Solution().isMatch("aa", "a*") is True
    assert Solution().isMatch("ab", "?*") is True
    assert Solution().isMatch("aab", "c*a*b") is False

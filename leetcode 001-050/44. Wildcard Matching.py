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
        if len(s) == 0:
            i = 0
            while i < len(p):
                if p[i] != "*":
                    return False
                i += 1
            return True
        if len(p) == 0:
            return False
        if s[0] == p[0] or p[0] == "?":
            return self.isMatch(s[1:], p[1:])
        elif p[0] == "*":
            i = 0
            while i < len(s):
                if self.isMatch(s[i:], p[1:]) or len(p[1:]) == 0:
                    return True
                i += 1
            return False
        else:
            return False


if __name__ == "__main__":
    assert Solution().isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab",
                              "***bba**a*bbba**aab**b") is False
    assert Solution().isMatch("ho", "ho**") is True
    assert Solution().isMatch("aa", "a") is False
    assert Solution().isMatch("aa", "aa") is True
    assert Solution().isMatch("aaa", "aa") is False
    assert Solution().isMatch("aa", "*") is True
    assert Solution().isMatch("aa", "a*") is True
    assert Solution().isMatch("ab", "?*") is True
    assert Solution().isMatch("aab", "c*a*b") is False

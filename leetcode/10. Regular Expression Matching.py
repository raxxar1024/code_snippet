class Solution(object):
    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        result = [[False for i in xrange(len(p) + 1)] for j in xrange(len(s) + 1)]

        result[0][0] = True

        for i in xrange(2, len(p) + 1):
            if p[i - 1] == '*':
                result[0][i] = result[0][i - 2]

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != "*":
                    if result[i - 1][j - 1] is True and (s[i - 1] == p[j - 1] or p[j - 1] == "."):
                        result[i][j] = True
                else:
                    if s[i - 1] != p[j - 2]:
                        result[i][j] = result[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        result[i][j] = result[i - 1][j]

                    if result[i][j-2] is True:
                        result[i][j] = True

        return result[-1][-1]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        if len(p) == 1:
            if len(s) == 1 and (p[0] == s[0] or p[0] == '.'):
                return True
            else:
                return False

        if p[1] != "*":
            if len(s) == 0:
                return False
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])
        else:
            while len(s) != 0 and (s[0] == p[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])


if __name__ == "__main__":
    assert Solution().isMatch("aa", "a") is False
    assert Solution().isMatch("aa", "aa") is True
    assert Solution().isMatch("aaa", "aa") is False
    assert Solution().isMatch("aa", "a*") is True
    assert Solution().isMatch("aa", ".*") is True
    assert Solution().isMatch("ab", ".*") is True
    assert Solution().isMatch("aab", "c*a*b") is True
    assert Solution().isMatch("aaa", "ab*a*c*a") is True

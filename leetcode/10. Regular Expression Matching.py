class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        result = [[False for i in xrange(len(p)+1)] for j in xrange(len(s)+1)]

        result[0][0] = True

        for i in xrange(2, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-2]

        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                if p[j-1] != "*":
                    if result[i-1][j-1] is True and (s[i-1] == p[j-1] or p[j-1] == "."):
                        result[i][j] = True
                else:
                    if s[i-1] != p[j-2]:
                        result[i][j] = result[i][j-2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        result[i][j] = result[i-1][j]

        return result[-1][-1]


if __name__ == "__main__":
    assert Solution().isMatch("aa","a") == False
    assert Solution().isMatch("aa","aa") == True
    assert Solution().isMatch("aaa","aa") == False
    assert Solution().isMatch("aa","a*") == True
    assert Solution().isMatch("aa", ".*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True


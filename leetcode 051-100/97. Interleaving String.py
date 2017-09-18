"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        match = [[False for _ in xrange(len(s1) + 1)] for _ in xrange(len(s2) + 1)]
        match[0][0] = True
        for i in xrange(1, len(s1) + 1):
            match[0][i] = match[0][i - 1] and s1[i - 1] == s3[i - 1]
        for i in xrange(1, len(s2) + 1):
            match[i][0] = match[i - 1][0] and s2[i - 1] == s3[i - 1]

        for i in xrange(1, len(s1) + 1):
            for j in xrange(1, len(s2) + 1):
                match[j][i] = (match[j][i - 1] and s1[i - 1] == s3[i + j - 1]) or (
                match[j - 1][i] and s2[j - 1] == s3[i + j - 1])

        return match[-1][-1]


if __name__ == "__main__":
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") is False

"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        df = [[0 for _ in xrange(len(t) + 1)] for _ in xrange(len(s) + 1)]
        for i in xrange(len(s) + 1):
            df[i][0] = 1

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(t) + 1):
                df[i][j] = df[i-1][j]
                if s[i-1] == t[j-1]:
                    df[i][j] += df[i-1][j-1]
        return df[-1][-1]


if __name__ == "__main__":
    assert Solution().numDistinct("rabbbit", "rabbit") == 3

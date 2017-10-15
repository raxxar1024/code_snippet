"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in xrange(len(s) + 1)]
        p = [[False for _ in xrange(len(s))] for _ in xrange(len(s))]

        for i in xrange(len(s) + 1):
            dp[i] = len(s) - i

        for i in xrange(len(s) - 1, -1, -1):
            for j in xrange(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1]):
                    p[i][j] = True
                    dp[i] = min(dp[j + 1] + 1, dp[i])

        return dp[0] - 1


if __name__ == "__main__":
    assert Solution().minCut("bb") == 0
    assert Solution().minCut("aab") == 1

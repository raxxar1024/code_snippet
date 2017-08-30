"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        distance = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(m + 1):
            distance[i][0] = i
        for i in xrange(n + 1):
            distance[0][i] = i
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    tmp = distance[i - 1][j - 1]
                else:
                    tmp = distance[i - 1][j - 1] + 1
                distance[i][j] = min(tmp, min(distance[i - 1][j] + 1, distance[i][j - 1] + 1))

        return distance[-1][-1]


if __name__ == "__main__":
    assert Solution().minDistance("abc", "dcb") == 3
    assert Solution().minDistance("abc", "bcd") == 2
    assert Solution().minDistance("abc", "def") == 3
    assert Solution().minDistance("", "") == 0

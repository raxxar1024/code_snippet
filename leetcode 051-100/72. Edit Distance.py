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


if __name__ == "__main__":
    assert Solution().minDistance("abc", "dcb") == 3
    assert Solution().minDistance("abc", "bcd") == 2
    assert Solution().minDistance("abc", "def") == 3
    assert Solution().minDistance("", "") == 0

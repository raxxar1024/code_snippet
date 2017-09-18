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
        len_1, len_2, len_3 = len(s1), len(s2), len(s3)
        if len_1 + len_2 != len_3:
            return False
        if len_3 == 0:
            return True
        ret_1, ret_2 = False, False
        if len_1 == 0:
            if s2 == s3:
                return True
            else:
                return False
        if len_2 == 0:
            if s1 == s3:
                return True
            else:
                return False

        if s1[0] == s3[0]:
            ret_1 = self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]:
            ret_2 = self.isInterleave(s1, s2[1:], s3[1:])

        return ret_1 or ret_2


if __name__ == "__main__":
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") is False

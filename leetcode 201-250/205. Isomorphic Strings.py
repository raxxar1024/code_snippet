"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag_s = ["0" for _ in xrange(len(s))]
        flag_t = ["0" for _ in xrange(len(t))]
        dict_s = {}
        dict_t = {}

        for i in xrange(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = str(i)
            flag_s[i] = dict_s[s[i]]
            if t[i] not in dict_t:
                dict_t[t[i]] = str(i)
            flag_t[i] = dict_t[t[i]]
        return flag_s == flag_t


if __name__ == "__main__":
    assert Solution().isIsomorphic("egg", "add") is True
    assert Solution().isIsomorphic("foo", "bar") is False
    assert Solution().isIsomorphic("paper", "title") is True

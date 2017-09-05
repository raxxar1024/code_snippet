"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start, end, min_start, min_end = 0, 0, 0, len(s)+1
        dict_t_standard, dict_t = {}, {}
        for word in t:
            if word in dict_t_standard:
                dict_t_standard[word] += 1
            else:
                dict_t_standard[word] = 1
                dict_t[word] = 0

        def check_dict(d1, d2):
            for k in d1:
                if d1[k] > d2[k]:
                    return False
            return True

        for i in xrange(len(s)):
            if s[i] in dict_t:
                dict_t[s[i]] += 1
            while check_dict(dict_t_standard, dict_t):
                if i - start < min_end - min_start:
                    min_start, min_end = start, i
                if s[start] in dict_t:
                    dict_t[s[start]] -= 1
                start += 1

        if (min_end - min_start) > len(s):
            return ""
        else:
            return s[min_start:min_end + 1]


if __name__ == "__main__":
    assert Solution().minWindow("a", "aa") == ""
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"

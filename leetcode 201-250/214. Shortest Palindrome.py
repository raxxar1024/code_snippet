"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
Thanks to @Freezen for additional test cases.

"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_s = s[::-1]
        max_len = 0
        for i in xrange(len(s) + 1):
            if s[:i] == s[i - 1::-1]:
                max_len = i
        return rev_s[:len(s) - max_len] + s


if __name__ == "__main__":
    assert Solution().shortestPalindrome("aba") == "aba"
    assert Solution().shortestPalindrome("a") == "a"
    assert Solution().shortestPalindrome("aacecaaa") == "aaacecaaa"
    assert Solution().shortestPalindrome("abcd") == "dcbabcd"

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
        l = s + "#" + rev_s

        def get_next():
            next_list = [-1] * len(l)
            j = 0
            k = -1
            while j < len(l) - 1:
                if k == -1 or l[j] == l[k]:
                    j += 1
                    k += 1
                    next_list[j] = k
                else:
                    k = next_list[k]
            return next_list[-1]

        max_len = get_next()
        return s[max_len + 1:][::-1] + s


if __name__ == "__main__":
    assert Solution().shortestPalindrome("aba") == "aba"
    assert Solution().shortestPalindrome("a") == "a"
    assert Solution().shortestPalindrome("aacecaaa") == "aaacecaaa"
    assert Solution().shortestPalindrome("abcd") == "dcbabcd"

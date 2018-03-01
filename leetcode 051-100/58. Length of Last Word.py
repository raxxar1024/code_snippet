"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(" ")
        length = 0
        for i in reversed(xrange(len(words))):
            if len(words[i]) != 0:
                length = len(words[i])
                break
        return length


if __name__ == "__main__":
    assert Solution().lengthOfLastWord("Today is a nice day") == 3
    assert Solution().lengthOfLastWord("H  ") == 1
    assert Solution().lengthOfLastWord("Hello World") == 5

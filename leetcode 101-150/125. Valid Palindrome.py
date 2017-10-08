"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_char(c):
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'):
                return True
            else:
                return False

        left, right = 0, len(s) - 1
        while left < right:
            if not is_char(s[left]):
                left += 1
                continue
            if not is_char(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


if __name__ == "__main__":
    assert Solution().isPalindrome(",P") is True
    assert Solution().isPalindrome("0P") is False
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
    assert Solution().isPalindrome("race a car") is False
    assert Solution().isPalindrome("") is True

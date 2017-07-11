class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


if __name__ == "__main__":
    assert Solution().isValid("[") is False
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False




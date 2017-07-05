class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """


if __name__ == "__main__":
    assert Solution().romanToInt("I") == 1
    assert Solution().romanToInt("CXXIII") == 123
    assert Solution().romanToInt("MCCXXXIV") == 1234

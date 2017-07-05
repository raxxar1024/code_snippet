class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """


if __name__ == "__main__":
    assert Solution().intToRoman(1) is "I"
    assert Solution().intToRoman(123) is "CXXIII"
    assert Solution().intToRoman(1234) is "MCCXXXIV"

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        i = num / 1000
        j = num % 1000
        tmp = "M" * i

        i = j / 100
        j %= 100
        if 0 < i < 4:
            tmp += "C" * i
        elif i == 4:
            tmp += "CD"
        elif 4 < i < 9:
            tmp += "D" * (i / 5) + "C" * (i % 5)
        elif i == 9:
            tmp += "CM"

        i = j / 10
        j %= 10
        if 0 < i < 4:
            tmp += "X" * i
        elif i == 4:
            tmp += "XL"
        elif 4 < i < 9:
            tmp += "L" * (i / 5) + "X" * (i % 5)
        elif i == 9:
            tmp += "XC"

        i = j
        if 0 < i < 4:
            tmp += "I" * i
        elif i == 4:
            tmp += "IV"
        elif 4 < i < 9:
            tmp += "V" * (i / 5) + "I" * (i % 5)
        elif i == 9:
            tmp += "IX"

        return tmp

if __name__ == "__main__":
    assert Solution().intToRoman(1) == "I"
    assert Solution().intToRoman(123) == "CXXIII"
    assert Solution().intToRoman(1234) == "MCCXXXIV"

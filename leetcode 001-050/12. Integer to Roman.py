class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_array = [
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM", "*",  "*",  "*",  "*",  "*",    "*"],
        ]

        tmp = roman_array[3][(num / 1000)]
        tmp += roman_array[2][(num % 1000 / 100)]
        tmp += roman_array[1][(num % 100 / 10)]
        tmp += roman_array[0][(num % 10)]

        return tmp

if __name__ == "__main__":
    assert Solution().intToRoman(1) == "I"
    assert Solution().intToRoman(123) == "CXXIII"
    assert Solution().intToRoman(1234) == "MCCXXXIV"

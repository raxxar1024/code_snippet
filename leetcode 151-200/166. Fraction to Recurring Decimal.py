"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

Credits:
Special thanks to @Shangrila for adding this problem and creating all test cases.

"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """


if __name__ == "__main__":
    assert Solution().fractionToDecimal(1, 2) == "0.5"
    assert Solution().fractionToDecimal(2, 1) == "2"
    assert Solution().fractionToDecimal(2, 3) == "0.(6)"

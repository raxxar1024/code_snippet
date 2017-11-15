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
        result = ""
        if numerator * denominator < 0:
            result = "-"

        dividend, divisor = abs(numerator), abs(denominator)
        result += str(dividend / divisor)

        lookups = {}
        remainder = dividend % divisor
        if remainder != 0:
            result += "."
        while remainder != 0 and remainder not in lookups:
            result += str(remainder * 10 / divisor)
            lookups[remainder] = len(result) - 1
            remainder = remainder * 10 % divisor

        if remainder in lookups:
            result = result[:lookups[remainder]] + "(" + result[lookups[remainder]:] + ")"

        return result


if __name__ == "__main__":
    assert Solution().fractionToDecimal(1, 90) == "0.0(1)"
    assert Solution().fractionToDecimal(1, 2) == "0.5"
    assert Solution().fractionToDecimal(2, 1) == "2"
    assert Solution().fractionToDecimal(2, 3) == "0.(6)"

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        multiply = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                multiply[i + j] += (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))

        for i in xrange(len(multiply) - 1):
            multiply[i + 1] += multiply[i] / 10
            multiply[i] %= 10

        i = len(multiply) - 1
        is_start = False
        result = ""
        while i >= 0:
            if multiply[i] != 0 or is_start is True:
                is_start = True
                result += chr(multiply[i] + ord("0"))
            i -= 1

        return result if result != "" else "0"


if __name__ == "__main__":
    assert Solution().multiply("0", "0") == "0"
    assert Solution().multiply("99", "99") == "9801"
    assert Solution().multiply("11", "12") == "132"

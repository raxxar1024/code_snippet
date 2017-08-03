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
                tmp = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                multiply[i + j] += tmp
                multiply[i + j + 1] += multiply[i + j]/10
                multiply[i + j] %= 10

        def int2chr(ch):
            return chr(ch + ord("0"))

        result = "".join(map(int2chr, multiply[::-1]))

        for i in xrange(len(result)):
            if result[i] != "0":
                return result[i:]
        return "0"


if __name__ == "__main__":
    assert Solution().multiply("0", "0") == "0"
    assert Solution().multiply("99", "99") == "9801"
    assert Solution().multiply("11", "12") == "132"

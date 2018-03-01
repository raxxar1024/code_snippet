"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry, result, a, b = 0, "", a[::-1], b[::-1]
        for i in xrange(max(len(a), len(b))):
            tmp = carry
            if i < len(a):
                tmp += int(a[i])
            if i < len(b):
                tmp += int(b[i])
            carry = tmp / 2
            result += str(tmp % 2)
        if carry == 1:
            result += "1"
        return result[::-1]


if __name__ == "__main__":
    assert Solution().addBinary("10", "1") == "11"
    assert Solution().addBinary("11", "1") == "100"

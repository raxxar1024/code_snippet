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
        len_a, len_b = len(a), len(b)
        if len_a > len_b:
            b = "0" * (len_a - len_b) + b
        else:
            a = "0" * (len_b - len_a) + a

        carry = 0
        tmp = [0] * max(len_a, len_b)
        for i in reversed(xrange(max(len_a, len_b))):
            tmp[i] = int(a[i]) + int(b[i]) + carry
            carry = tmp[i] / 2
            tmp[i] %= 2
        if carry == 1:
            tmp = [1] + tmp

        result = ""
        for i in xrange(len(tmp)):
            result += str(tmp[i])

        return result




if __name__ == "__main__":
    assert Solution().addBinary("11", "1") == "100"

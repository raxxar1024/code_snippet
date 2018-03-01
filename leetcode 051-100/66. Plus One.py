"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        digits[-1] += 1
        for i in reversed(xrange(len(digits))):
            digits[i] += carry
            carry = digits[i] / 10
            digits[i] %= 10

        if carry == 1:
            return [1] + digits
        else:
            return digits


if __name__ == "__main__":
    assert Solution().plusOne([1, 0]) == [1, 1]
    assert Solution().plusOne([9, 9]) == [1, 0, 0]
    assert Solution().plusOne([0]) == [1]

"""
Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 2**31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

"""


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """


if __name__ == "__main__":
    assert Solution().numberToWords(123) == "One Hundred Twenty Three"
    assert Solution().numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert Solution().numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

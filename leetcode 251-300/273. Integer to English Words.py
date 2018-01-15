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
        if num == 0:
            return "Zero"
        less_than_20 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                        "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def numberToWords_3bit(num):
            if num == 0:
                return ""
            tmp = ""
            if num >= 100:
                tmp += less_than_20[num / 100 - 1] + " Hundred "
                num %= 100
            if num > 19:
                tmp += tens[num / 10 - 2]
                if num % 10 != 0:
                    tmp += " %s" % less_than_20[num % 10 - 1]
            elif 0 < num < 20:
                tmp += less_than_20[num - 1]
            return tmp[:-1] if tmp[-1] == " " else tmp

        tmp = ""
        if num >= 1000000000:
            tmp += "%s Billion " % numberToWords_3bit(num / 1000000000)
            num %= 1000000000
        if num >= 1000000:
            tmp += "%s Million " % numberToWords_3bit(num / 1000000)
            num %= 1000000
        if num >= 1000:
            tmp += "%s Thousand " % numberToWords_3bit(num / 1000)
            num %= 1000
        tmp += numberToWords_3bit(num)

        return tmp[:-1] if tmp[-1] == " " else tmp


if __name__ == "__main__":
    assert Solution().numberToWords(100000) == "One Hundred Thousand"
    assert Solution().numberToWords(20) == "Twenty"
    assert Solution().numberToWords(0) == "Zero"
    assert Solution().numberToWords(1) == "One"
    assert Solution().numberToWords(100) == "One Hundred"
    assert Solution().numberToWords(123) == "One Hundred Twenty Three"
    assert Solution().numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert Solution().numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

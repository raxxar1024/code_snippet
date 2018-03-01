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
        lookups = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                   10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                   17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
                   50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        unit = ["", "Thousand", "Million", "Billion"]
        res, i = [], 0
        while num > 0:
            if num % 1000:
                res.append(self.three_digits(num % 1000, lookups, unit[i]))
            i += 1
            num /= 1000
        return " ".join(res[::-1])

    def three_digits(self, num, lookups, unit):
        res = []
        if num // 100:
            res.append(lookups[num // 100] + " Hundred")
        if num % 100:
            res.append(self.two_digits(num % 100, lookups))
        if unit != "":
            res.append(unit)
        return " ".join(res)

    def two_digits(self, num, lookups):
        if num in lookups:
            return lookups[num]
        return lookups[num // 10 * 10] + " " + lookups[num % 10]


if __name__ == "__main__":
    assert Solution().numberToWords(100000) == "One Hundred Thousand"
    assert Solution().numberToWords(20) == "Twenty"
    assert Solution().numberToWords(0) == "Zero"
    assert Solution().numberToWords(1) == "One"
    assert Solution().numberToWords(100) == "One Hundred"
    assert Solution().numberToWords(123) == "One Hundred Twenty Three"
    assert Solution().numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert Solution().numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.

"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result, dvd = "", n

        while dvd > 0:
            result += chr((dvd - 1) % 26 + ord("A"))
            dvd = (dvd - 1) / 26

        return result[::-1]


if __name__ == "__main__":
    assert Solution().convertToTitle(27) == "AA"
    assert Solution().convertToTitle(52) == "AZ"
    assert Solution().convertToTitle(1) == "A"
    assert Solution().convertToTitle(28) == "AB"

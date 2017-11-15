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


if __name__ == "__main__":
    assert Solution().convertToTitle(1) == "A"
    assert Solution().convertToTitle(28) == "AB"

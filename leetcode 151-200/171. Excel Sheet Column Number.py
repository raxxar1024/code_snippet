"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            result = result * 26 + ord(c) - ord("A") + 1
        return result


if __name__ == "__main__":
    assert Solution().titleToNumber("AA") == 27
    assert Solution().titleToNumber("AZ") == 52
    assert Solution().titleToNumber("A") == 1
    assert Solution().titleToNumber("AB") == 28

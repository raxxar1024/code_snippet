"""
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or *
between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

Credits:
Special thanks to @davidtan1890 for adding this problem and creating all test cases.

"""


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """


if __name__ == "__main__":
    assert Solution().addOperators("123", 6) == ["1+2+3", "1*2*3"]
    assert Solution().addOperators("232", 8) == ["2*3+2", "2+3*2"]
    assert Solution().addOperators("105", 5) == ["1*0+5", "10-5"]
    assert Solution().addOperators("00", 0) == ["0+0", "0-0", "0*0"]
    assert Solution().addOperators("3456237490", 9191) == []

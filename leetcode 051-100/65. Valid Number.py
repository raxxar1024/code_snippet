"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.

"""


class InputType:
    INVALID = 0
    SPACE = 1
    SIGN = 2
    DIGIT = 3
    DOT = 4
    EXPONENT = 5


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        transition_table = [
            [-1, 0, 3, 1, 2, -1],  # next states for state 0
            [-1, 8, -1, 1, 4, 5],  # next states for state 1
            [-1, -1, -1, 4, -1, -1],  # next states for state 2
            [-1, -1, -1, 1, 2, -1],  # next states for state 3
            [-1, 8, -1, 4, -1, 5],  # next states for state 4
            [-1, -1, 6, 7, -1, -1],  # next states for state 5
            [-1, -1, -1, 7, -1, -1],  # next states for state 6
            [-1, 8, -1, 7, -1, -1],  # next states for state 7
            [-1, 8, -1, -1, -1, -1]  # next states for state 8
        ]

        state = 0
        for c in s:
            input_type = InputType.INVALID
            if c.isspace():
                input_type = InputType.SPACE
            elif c == "+" or c == "-":
                input_type = InputType.SIGN
            elif c.isdigit():
                input_type = InputType.DIGIT
            elif c == ".":
                input_type = InputType.DOT
            elif c == "e" or c == "E":
                input_type = InputType.EXPONENT
            state = transition_table[state][input_type]
            if state == -1:
                return False

        return state == 1 or state == 4 or state == 7 or state == 8


if __name__ == "__main__":
    assert Solution().isNumber("0") is True
    assert Solution().isNumber("0.1") is True
    assert Solution().isNumber("abc") is False
    assert Solution().isNumber("1 a") is False
    assert Solution().isNumber("2e10") is True

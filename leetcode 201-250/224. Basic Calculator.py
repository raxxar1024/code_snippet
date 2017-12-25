"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operators, operands = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i - 1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] in ["+", "-", ")"]:
                operators.append(s[i])
            elif s[i] == "(":
                while operators[-1] != ")":
                    self.compute(operators, operands)
                operators.pop()

        while operators:
            self.compute(operators, operands)
        return operands[-1]

    def compute(self, operators, operands):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == "+":
            operands.append(left + right)
        elif op == "-":
            operands.append(left - right)


if __name__ == "__main__":
    assert Solution().calculate("0") == 0
    assert Solution().calculate("1 + 1") == 2
    assert Solution().calculate(" 2-1 + 2 ") == 3
    assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23

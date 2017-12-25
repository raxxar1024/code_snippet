"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

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
            elif s[i] in [")", "*", "/"]:
                operators.append(s[i])
            elif s[i] in ["+", "-"]:
                while operators and (operators[-1] == "*" or operators[-1] == "/"):
                    self.compute(operators, operands)
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
        elif op == "*":
            operands.append(left * right)
        elif op == "/":
            operands.append(left / right)


if __name__ == "__main__":
    assert Solution().calculate("3+2*2") == 7
    assert Solution().calculate(" 3/2 ") == 1
    assert Solution().calculate(" 3+5 / 2 ") == 5

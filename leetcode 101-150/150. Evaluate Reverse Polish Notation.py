"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        operators = ["+", "-", "*", "/"]
        stack = []
        for i in xrange(len(tokens)):
            c = tokens[i]
            if c in operators:
                num_1 = stack.pop()
                num_2 = stack.pop()
                tmp = 0
                if c == "+":
                    tmp = num_2 + num_1
                elif c == "-":
                    tmp = num_2 - num_1
                elif c == "*":
                    tmp = num_2 * num_1
                elif c == "/":
                    tmp = abs(num_2) / abs(num_1)
                    if num_1 * num_2 < 0:
                        tmp *= -1
                stack.append(tmp)
            else:
                stack.append(int(tokens[i]))

        return stack[-1]


if __name__ == "__main__":
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6

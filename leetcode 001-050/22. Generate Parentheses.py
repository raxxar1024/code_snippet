class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def gen_string(left, right, s):
            if left == 0 and right == 0:
                result.append(s)
            if left > 0:
                gen_string(left-1, right, s+"(")
            if right > 0 and left < right:
                gen_string(left, right-1, s+")")
        gen_string(n, n, "")
        return result


if __name__ == "__main__":
    assert Solution().generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]

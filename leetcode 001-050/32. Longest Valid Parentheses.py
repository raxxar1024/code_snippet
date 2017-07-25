class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, stack, last = 0, [], -1
        for i in xrange(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    last = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        max_len = max(i-last, max_len)
                    else:
                        max_len = max(i-stack[-1], max_len)
        return max_len


if __name__ == "__main__":
    assert Solution().longestValidParentheses(")()())") == 4
    assert Solution().longestValidParentheses("(()") == 2
    assert Solution().longestValidParentheses("()(()") == 2
    assert Solution().longestValidParentheses("()") == 2




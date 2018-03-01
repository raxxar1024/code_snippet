class Solution(object):
    # stack
    def longestValidParentheses2(self, s):
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

    # dp
    def longestValidParentheses(self, s):
        dp = [0] * len(s)
        for i in xrange(len(s)-2, -1, -1):
            if s[i] == "(":
                if i + dp[i+1] + 1 < len(s) and s[i + dp[i+1] + 1] == ")":
                    dp[i] = dp[i+1] + 2
                    if i + dp[i+1] + 2 < len(s):
                        dp[i] += dp[i+dp[i]]

        max_len = 0
        for i in xrange(len(s)):
            max_len = max(max_len, dp[i])

        return max_len

if __name__ == "__main__":
    assert Solution().longestValidParentheses(")()())") == 4
    assert Solution().longestValidParentheses("(()") == 2
    assert Solution().longestValidParentheses("()(()") == 2
    assert Solution().longestValidParentheses("()") == 2




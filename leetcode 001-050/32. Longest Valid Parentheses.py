class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """


if __name__ == "__main__":
    Solution().longestValidParentheses("(()") == 2
    Solution().longestValidParentheses(")()())") == 4



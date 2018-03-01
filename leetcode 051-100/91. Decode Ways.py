"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or s[0] == "0":
            return 0
        dp = [1, 1]
        for i in xrange(2, len(s) + 1):
            num = int(s[i - 2:i])
            if num != 20 and 26 >= num > 10:
                dp.append(dp[i - 1] + dp[i - 2])
            elif num == 10 or num == 20:
                dp.append(dp[i - 2])
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[-1]


if __name__ == "__main__":
    assert Solution().numDecodings("230") == 0
    assert Solution().numDecodings("27") == 1
    assert Solution().numDecodings("12") == 2

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """


if __name__ == "__main__":
    assert Solution().partition("aab") == [
        ["aa", "b"],
        ["a", "a", "b"]
    ]

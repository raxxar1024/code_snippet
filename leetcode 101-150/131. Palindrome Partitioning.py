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
        result = []

        def get_partition(tmp_path, tmp_s):
            if not tmp_s:
                result.append(tmp_path)
                return
            for i in xrange(len(tmp_s)):
                if self.is_valid(tmp_s[:i + 1]):
                    get_partition(tmp_path + [tmp_s[:i + 1]], tmp_s[i + 1:])

        get_partition([], s)
        return result

    def is_valid(self, tmp_s):
        return tmp_s == tmp_s[::-1]


if __name__ == "__main__":
    assert Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"], ]

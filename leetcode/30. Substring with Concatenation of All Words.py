class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """


if __name__ == "__main__":
    assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]


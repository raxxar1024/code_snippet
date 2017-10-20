"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        result = []

        def is_valid(tmp_s, intermediate):
            if not tmp_s:
                result.append(intermediate[1:])
                return
            for i in xrange(len(tmp_s)):
                if tmp_s[:i + 1] in wordDict:
                    is_valid(tmp_s[i + 1:], intermediate + " " + tmp_s[:i + 1])

        is_valid(s, "")
        return result


if __name__ == "__main__":
    assert Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == ["cats and dog", "cat sand dog"]

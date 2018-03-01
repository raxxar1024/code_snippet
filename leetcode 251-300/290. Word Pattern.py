"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:
Special thanks to @minglotus6 for adding this problem and creating all test cases.

"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if len(words) != len(pattern):
            return False
        dict_pattern = {}
        for i in range(len(words)):
            if pattern[i] in dict_pattern:
                if dict_pattern[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in dict_pattern.values():
                    return False
                dict_pattern[pattern[i]] = words[i]
        return True


if __name__ == "__main__":
    assert Solution().wordPattern("abba", "dog cat cat dog") is True
    assert Solution().wordPattern("abba", "dog cat cat fish") is False
    assert Solution().wordPattern("aaaa", "dog cat cat dog") is False
    assert Solution().wordPattern("abba", "dog dog dog dog") is False

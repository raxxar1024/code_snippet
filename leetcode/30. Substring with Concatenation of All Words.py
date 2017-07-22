class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_count = len(words)
        word_len = len(words[0])
        string_len = len(s)
        result = []
        for i in xrange(0, string_len-word_count*word_len+1):
            words_copy = [item for item in words]
            if self.is_match(s[i:i+word_count*word_len], words_copy):
                result.append(i)
        return result

    def is_match(self, s, p):
        word_len = len(p[0])
        for i in xrange(0, len(s), word_len):
            try:
                idx = p.index(s[i:i+word_len])
            except ValueError:
                return False
            del p[idx]
        return True


if __name__ == "__main__":
    assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    assert Solution().findSubstring("barfoobarfoobarman", ["foo", "bar"]) == [0, 3, 6, 9]


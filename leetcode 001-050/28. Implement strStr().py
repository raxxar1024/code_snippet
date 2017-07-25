class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if haystack == "":
            return -1
        return self.KMP(haystack, needle)

    def KMP(self, string, pattern):
        j = -1
        list_next = self.get_next(pattern)
        for i in xrange(len(string)):
            while j > -1 and pattern[j+1] != string[i]:
                j = list_next[j]
            if pattern[j+1] == string[i]:
                j += 1
            if j == len(pattern)-1:
                return i-j
        return -1

    def get_next(self, pattern):
        list_next = [-1] * len(pattern)
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j+1] != pattern[i]:
                j = list_next[j]
            if pattern[j+1] == pattern[i]:
                j += 1
            list_next[i] = j
        return list_next
                

if __name__ == "__main__":
    assert Solution().strStr("123", "23") == 1
    assert Solution().strStr("", "a") == -1
    assert Solution().strStr("", "") == 0
    assert Solution().strStr("a", "") == 0

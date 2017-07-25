class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_len = len(strs[0])
        for o_str in strs:
            min_len = min(len(o_str), min_len)

        tmp = ""
        for i in xrange(min_len):
            for o_str in strs[1:]:
                if o_str[i] != strs[0][i]:
                    return tmp
            tmp += strs[0][i]
        return tmp

if __name__ == "__main__":
    assert Solution().longestCommonPrefix([]) == ""
    assert Solution().longestCommonPrefix(["123", "1", "122"]) == "1"
    assert Solution().longestCommonPrefix(["123", "1", "q22"]) == ""
    assert Solution().longestCommonPrefix(["123"]) == "123"
    assert Solution().longestCommonPrefix(["123", "123"]) == "123"



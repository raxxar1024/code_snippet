class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst_s = list(s)
        lst_tmp = []
        count_tmp = 0
        count_max = 0
        for item in lst_s:
            try:
                idx = lst_tmp.index(item)
            except:
                idx = -1
            if idx != -1:
                for i in range(0, idx+1):
                    del lst_tmp[0]
                count_tmp -= (idx+1)
            count_tmp += 1
            lst_tmp.append(item)
            if count_tmp > count_max:
                count_max = count_tmp
        return count_max


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("a") == 1
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring("auak") == 3

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp_stack = []
        dict_pair = {"[": "]", "{": "}", "(": ")"}
        for c in s:
            if c in dict_pair:
                tmp_stack.append(c)
            else:
                if len(tmp_stack) == 0 or dict_pair[tmp_stack.pop()] != c:
                    return False
        return len(tmp_stack) == 0

if __name__ == "__main__":
    assert Solution().isValid("[") is False
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False




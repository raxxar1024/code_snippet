class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp_stack = []
        dict_pair = {"]": "[", "}": "{", ")": "(", }
        lst_left = ["[", "{", "("]
        for c in s:
            if c in lst_left:
                tmp_stack.append(c)
            else:
                if len(tmp_stack) == 0:
                    return False
                tmp = tmp_stack.pop()
                if tmp != dict_pair[c]:
                    return False

        if len(tmp_stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    assert Solution().isValid("[") is False
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False




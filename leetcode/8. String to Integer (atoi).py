class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is "":
            return 0
        return int(str)


if __name__ == "__main__":
    assert Solution().myAtoi("") == 0

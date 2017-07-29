class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """


if __name__ == "__main__":
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(2) == "11"
    assert Solution().countAndSay(3) == "21"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
    assert Solution().countAndSay(6) == "312211"
    assert Solution().countAndSay(11) == "11131221133112132113212221"

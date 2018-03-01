class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def convert(s):
            last, count, tmp_string = '', 0, ''
            for j in xrange(len(s)):
                if s[j] != last:
                    if count != 0:
                        tmp_string += chr(ord('0')+count) + last
                    last, count = s[j], 1
                else:
                    count += 1
            tmp_string += chr(ord('0')+count) + last
            return tmp_string

        s = "1"
        for i in xrange(2, n+1):
            s = convert(s)
        return s

if __name__ == "__main__":
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(2) == "11"
    assert Solution().countAndSay(3) == "21"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
    assert Solution().countAndSay(6) == "312211"
    assert Solution().countAndSay(11) == "11131221133112132113212221"

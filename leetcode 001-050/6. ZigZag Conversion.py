class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        t = ""
        step = 2 * (numRows - 1)

        for i in xrange(0, numRows):
            for j in xrange(0, len(s), step):
                if j+i >= len(s):
                    break
                t += s[j+i]
                if i != 0 and i != numRows-1 and j+step-i < len(s):
                    t += s[j+step-i]

        return t


if __name__ == "__main__":
    # assert Solution().convert("0123456789", 4) == "0615724839"
    assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

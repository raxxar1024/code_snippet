class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }

        tmp = dict_roman[s[0]]
        for i in xrange(1, len(s)):
            tmp += dict_roman[s[i]]
            if dict_roman[s[i]] > dict_roman[s[i-1]]:
                tmp -= 2 * dict_roman[s[i-1]]

        return tmp

if __name__ == "__main__":
    assert Solution().romanToInt("I") == 1
    assert Solution().romanToInt("CXXIII") == 123
    assert Solution().romanToInt("MCCXXXIV") == 1234

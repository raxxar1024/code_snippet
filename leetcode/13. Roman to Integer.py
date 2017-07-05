class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.startswith("IV"):
            return 4+self.romanToInt(s[2:])
        if s.startswith("IX"):
            return 9+self.romanToInt(s[2:])
        if s.startswith("XL"):
            return 40+self.romanToInt(s[2:])
        if s.startswith("XC"):
            return 90+self.romanToInt(s[2:])
        if s.startswith("CD"):
            return 400+self.romanToInt(s[2:])
        if s.startswith("CM"):
            return 900+self.romanToInt(s[2:])
        if s.startswith("I"):
            return 1+self.romanToInt(s[1:])
        if s.startswith("V"):
            return 5+self.romanToInt(s[1:])
        if s.startswith("X"):
            return 10+self.romanToInt(s[1:])
        if s.startswith("L"):
            return 50+self.romanToInt(s[1:])
        if s.startswith("C"):
            return 100+self.romanToInt(s[1:])
        if s.startswith("D"):
            return 500+self.romanToInt(s[1:])
        if s.startswith("M"):
            return 1000+self.romanToInt(s[1:])
        if s == "":
            return 0

if __name__ == "__main__":
    assert Solution().romanToInt("I") == 1
    assert Solution().romanToInt("CXXIII") == 123
    assert Solution().romanToInt("MCCXXXIV") == 1234

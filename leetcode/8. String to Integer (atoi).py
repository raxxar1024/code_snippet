class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if len(str) == 0:
            return 0
        value, count, minus, start = 0, 0, 1, 0
        MAX_VAL = 0x7fffffff
        MIN_VAL = -1*0x80000000
        for i in xrange(0, len(str)):
            if str[i] != " ":
                start = i
                break

        for i in xrange(start, len(str)):
            try:
                tmp = int(str[i])
            except:
                count += 1
                if str[i] == "+" and i == start:
                    continue
                if str[i] == "-" and i == start:
                    continue
                if str[i] != " ":
                    break
                if count == 2:
                    break
                if i > start:
                    break
                continue
            value = value*10 + tmp

        if str[start] == "-":
            minus = -1

        ret = minus * value

        if MIN_VAL <= ret <= MAX_VAL:
            return ret

        if ret > MAX_VAL:
            return MAX_VAL
        if ret < MIN_VAL:
            return MIN_VAL


if __name__ == "__main__":
    assert Solution().myAtoi("") == 0
    assert Solution().myAtoi("+100") == 100
    assert Solution().myAtoi("+100+1000") == 100
    assert Solution().myAtoi("-100") == -100
    assert Solution().myAtoi("-100") == -100
    assert Solution().myAtoi("-100+1000") == -100
    assert Solution().myAtoi("-+100") == 0
    assert Solution().myAtoi("-1") == -1
    assert Solution().myAtoi("     100") == 100
    assert Solution().myAtoi("   +0 123") == 0
    assert Solution().myAtoi("    -00134") == -134
    assert Solution().myAtoi("2147483648") == 2147483647
    assert Solution().myAtoi("23a8f") == 23
    assert Solution().myAtoi(" b11228552307") == 0
    assert Solution().myAtoi("+1") == 1


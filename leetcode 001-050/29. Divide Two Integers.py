class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        positive = (dividend < 0) is (divisor < 0)
        result, dividend, divisor = 0, abs(dividend), abs(divisor)
        while dividend >= divisor:
            tmp = divisor
            move_count = 0
            while dividend >= tmp:
                dividend -= tmp
                result += (1 << move_count)
                tmp <<= 1
                move_count += 1

        if positive:
            return min(((1 << 31)-1), result)
        else:
            return max(-(1 << 31), -result)


if __name__ == "__main__":
    assert Solution().divide(-1, 1) == -1
    assert Solution().divide(-2147483648, 1) == -2147483648
    assert Solution().divide(-2147483648, -1) == 2147483647
    assert Solution().divide(1, 1) == 1
    assert Solution().divide(1, 2) == 0
    assert Solution().divide(23, 5) == 4
    assert Solution().divide(4, 2) == 2
    assert Solution().divide(0, 1) == 0
    assert Solution().divide(1, 0) == -1

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        if dividend == 0:
            return 0
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        move_count = 0
        while (divisor << move_count) <= dividend:
            move_count += 1

        if move_count == 0:
            return 0

        result = 0
        move_count -= 1
        while move_count >= 0:
            while (dividend - (divisor << move_count)) >= 0:
                result += (1 << move_count)
                dividend -= (divisor << move_count)
            move_count -= 1

        MAX_INT = (1 << 31) - 1
        MIN_INT = -(1 << 31)

        if positive:
            if result > MAX_INT:
                result = MAX_INT
            return result
        else:
            if -result < MIN_INT:
                result = -MIN_INT
            return -result


if __name__ == "__main__":
    assert Solution().divide(-2147483648, 1) == -2147483648
    assert Solution().divide(-2147483648, -1) == 2147483647
    assert Solution().divide(1, 1) == 1
    assert Solution().divide(1, 2) == 0
    assert Solution().divide(23, 5) == 4
    assert Solution().divide(4, 2) == 2
    assert Solution().divide(0, 1) == 0
    assert Solution().divide(1, 0) == -1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # str_x = str(x)
        # minus = False
        # if str_x[0] == "-":
        #     minus = True
        #     str_x = str_x[1:]
        # lst_x = list(str_x)
        # lst_x.reverse()
        # str_x_tmp = ''.join(lst_x)
        # if int(str_x_tmp) > 0x7fffffff:
        #     return 0
        # if minus is True:
        #     return -1 * int(str_x_tmp)
        # else:
        #     return int(str_x_tmp)
        tmp = 0
        if str(x)[0] is "-":
            tmp = -1 * int(str(x)[::-1][:-1])
        else:
            tmp = int(str(x)[::-1])

        if abs(tmp) > 0x7fffffff:
            return 0
        else:
            return tmp


if __name__ == "__main__":
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(1534236469) == 0

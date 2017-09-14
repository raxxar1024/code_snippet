"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def depart_string(part1, middle, n):
            if (len(s) - middle) > n * 3:
                return
            if middle > len(s) - 1:
                return
            if n == 1:
                if (len(s[middle:]) == 2 and int(s[middle:]) > 9) or \
                        (len(s[middle:]) == 3 and 256 > int(s[middle:]) > 99) or len(s[middle:]) == 1:
                    tmp = part1[1:] + "." + str(int(s[middle:]))
                    if tmp not in result:
                        result.append(tmp)
            else:
                if 100 <= int(s[middle:middle + 3]) <= 255:
                    depart_string(part1 + "." + str(int(s[middle:middle + 3])), middle + 3, n - 1)
                if int(s[middle:middle + 2]) >= 10:
                    depart_string(part1 + "." + str(int(s[middle:middle + 2])), middle + 2, n - 1)
                depart_string(part1 + "." + str(int(s[middle:middle + 1])), middle + 1, n - 1)
            return

        depart_string("", 0, 4)
        return result


if __name__ == "__main__":
    assert Solution().restoreIpAddresses("172162541") == ["0.100.1.0", "0.10.0.10"]
    assert Solution().restoreIpAddresses("010010") == ["0.100.1.0", "0.10.0.10"]
    assert Solution().restoreIpAddresses("0000") == ["0.0.0.0"]
    assert Solution().restoreIpAddresses("25525511135") == ["255.255.111.35", "255.255.11.135"]

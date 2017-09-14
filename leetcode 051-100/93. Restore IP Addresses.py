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


if __name__ == "__main__":
    assert Solution().restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"]

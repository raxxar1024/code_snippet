"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 13.37

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        lst_v1 = [int(x) for x in version1.split(".")]
        lst_v2 = [int(x) for x in version2.split(".")]

        while len(lst_v1) != len(lst_v2):
            if len(lst_v1) > len(lst_v2):
                lst_v2.append(0)
            else:
                lst_v1.append(0)

        return cmp(lst_v1, lst_v2)


if __name__ == "__main__":
    assert Solution().compareVersion("1.0", "1") == 0
    assert Solution().compareVersion("01", "1") == 0
    assert Solution().compareVersion("0.1", "1.1") == -1
    assert Solution().compareVersion("1.1", "1.2") == -1
    assert Solution().compareVersion("1.2", "13.37") == -1
    assert Solution().compareVersion("1.1", "1.1.1") == -1

"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result, words = [], path.split("/")

        for word in words:
            if word == ".." and result:
                result.pop()
            elif word != ".." and word != "." and word:
                result.append(word)

        return "/" + "/".join(result)


if __name__ == "__main__":
    assert Solution().simplifyPath("/home/../../..") == "/"
    assert Solution().simplifyPath("/") == "/"
    assert Solution().simplifyPath("/home/") == "/home"
    assert Solution().simplifyPath("/a/./b/../../c/") == "/c"
    assert Solution().simplifyPath("/../") == "/"
    assert Solution().simplifyPath("/home//foo/") == "/home/foo"

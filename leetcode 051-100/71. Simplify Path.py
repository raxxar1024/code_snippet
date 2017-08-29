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
        words = path.split("/")
        result_words_tmp = []

        for i in xrange(len(words)):
            if words[i] == "." or words[i] == "":
                continue
            else:
                result_words_tmp.append(words[i])

        if len(result_words_tmp) == 0:
            return "/"

        result_words = []
        for i in xrange(len(result_words_tmp)):
            if result_words_tmp[i] == "..":
                if len(result_words) != 0:
                    result_words.pop()
            else:
                result_words.append(result_words_tmp[i])

        return "/" + "/".join(result_words)


if __name__ == "__main__":
    assert Solution().simplifyPath("/home/../../..") == "/"
    assert Solution().simplifyPath("/") == "/"
    assert Solution().simplifyPath("/home/") == "/home"
    assert Solution().simplifyPath("/a/./b/../../c/") == "/c"
    assert Solution().simplifyPath("/../") == "/"
    assert Solution().simplifyPath("/home//foo/") == "/home/foo"

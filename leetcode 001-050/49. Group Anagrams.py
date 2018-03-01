"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import OrderedDict
        results = OrderedDict()
        result = []
        for o_str in strs:
            tmp = "".join(sorted(o_str))
            if tmp in results:
                results[tmp].append(o_str)
            else:
                results[tmp] = [o_str]

        for k, v in results.items():
            v.sort()
            result.append(v)

        return result

if __name__ == "__main__":
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["ate", "eat", "tea"],
        ["nat", "tan"],
        ["bat"]
    ]

"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        import collections
        sub_list = []
        for i in xrange(len(s) - 9):
            sub_list.append(s[i:i + 10])
        return [k for k, v in collections.Counter(sub_list).items() if v > 1]


if __name__ == "__main__":
    assert Solution().findRepeatedDnaSequences("AAAAAAAAAAA") == ["AAAAAAAAAA"]
    assert Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ["AAAAACCCCC", "CCCCCAAAAA"]

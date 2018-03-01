"""
Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings).
Please reload the code definition to get the latest changes.

"""


# https://discuss.leetcode.com/topic/8343/use-defaultdict-for-traceback-and-easy-writing-20-lines-python-code/9


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        import collections
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)

        level = set([beginWord])
        parents = collections.defaultdict(set)

        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for i in xrange(len(word)):
                    p1 = word[:i]
                    p2 = word[i + 1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            tmp = p1 + j + p2
                            if tmp in wordSet and tmp not in parents:
                                next_level[tmp].add(word)
            level = next_level
            parents.update(next_level)

        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p] + r for r in res for p in parents[r[0]]]

        return res


if __name__ == "__main__":
    # assert Solution().findLadders("qa", "sq",
    #                               ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le",
    #                                "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn",
    #                                "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc",
    #                                "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co",
    #                                "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an",
    #                                "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io",
    #                                "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]) == [
    #     ['qa', 'pa', 'pt', 'st', 'sq'], ['qa', 'la', 'lt', 'st', 'sq'], ['qa', 'ma', 'mt', 'st', 'sq'],
    #     ['qa', 'ca', 'cr', 'sr', 'sq'], ['qa', 'la', 'lr', 'sr', 'sq'], ['qa', 'fa', 'fr', 'sr', 'sq'],
    #     ['qa', 'ba', 'br', 'sr', 'sq'], ['qa', 'ma', 'mr', 'sr', 'sq'], ['qa', 'ca', 'ci', 'si', 'sq'],
    #     ['qa', 'na', 'ni', 'si', 'sq'], ['qa', 'la', 'li', 'si', 'sq'], ['qa', 'ta', 'ti', 'si', 'sq'],
    #     ['qa', 'pa', 'pi', 'si', 'sq'], ['qa', 'ba', 'bi', 'si', 'sq'], ['qa', 'ha', 'hi', 'si', 'sq'],
    #     ['qa', 'ma', 'mi', 'si', 'sq'], ['qa', 'pa', 'ph', 'sh', 'sq'], ['qa', 'ra', 'rh', 'sh', 'sq'],
    #     ['qa', 'ta', 'th', 'sh', 'sq'], ['qa', 'ca', 'co', 'so', 'sq'], ['qa', 'ga', 'go', 'so', 'sq'],
    #     ['qa', 'ta', 'to', 'so', 'sq'], ['qa', 'na', 'no', 'so', 'sq'], ['qa', 'la', 'lo', 'so', 'sq'],
    #     ['qa', 'pa', 'po', 'so', 'sq'], ['qa', 'ya', 'yo', 'so', 'sq'], ['qa', 'ma', 'mo', 'so', 'sq'],
    #     ['qa', 'ha', 'ho', 'so', 'sq'], ['qa', 'la', 'ln', 'sn', 'sq'], ['qa', 'ra', 'rn', 'sn', 'sq'],
    #     ['qa', 'ma', 'mn', 'sn', 'sq'], ['qa', 'ca', 'cm', 'sm', 'sq'], ['qa', 'ta', 'tm', 'sm', 'sq'],
    #     ['qa', 'pa', 'pm', 'sm', 'sq'], ['qa', 'fa', 'fm', 'sm', 'sq'], ['qa', 'ta', 'tc', 'sc', 'sq'],
    #     ['qa', 'na', 'nb', 'sb', 'sq'], ['qa', 'pa', 'pb', 'sb', 'sq'], ['qa', 'ra', 'rb', 'sb', 'sq'],
    #     ['qa', 'ya', 'yb', 'sb', 'sq'], ['qa', 'ma', 'mb', 'sb', 'sq'], ['qa', 'ta', 'tb', 'sb', 'sq'],
    #     ['qa', 'ga', 'ge', 'se', 'sq'], ['qa', 'la', 'le', 'se', 'sq'], ['qa', 'na', 'ne', 'se', 'sq'],
    #     ['qa', 'ra', 're', 'se', 'sq'], ['qa', 'ba', 'be', 'se', 'sq'], ['qa', 'ya', 'ye', 'se', 'sq'],
    #     ['qa', 'fa', 'fe', 'se', 'sq'], ['qa', 'ha', 'he', 'se', 'sq'], ['qa', 'ma', 'me', 'se', 'sq']
    # ]
    assert Solution().findLadders("hot", "dog", ["hot", "dog", "dot"]) == [
        ["hot", "dot", "dog"]
    ]
    assert Solution().findLadders("a", "c", ["a", "b", "c"]) == [
        ["a", "c"]
    ]
    assert Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == [
        ["hit", "hot", "lot", "log", "cog"],
        ["hit", "hot", "dot", "dog", "cog"],
    ]

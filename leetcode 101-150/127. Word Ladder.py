"""
Given two words (beginWord and endWord),
and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings).
Please reload the code definition to get the latest changes.

"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import collections
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)
        level = set([beginWord])
        parents = collections.defaultdict(set)

        count = 1
        while level and endWord not in parents:
            count += 1
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
        if res:
            return len(res[0])
        else:
            return 0


if __name__ == "__main__":
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 5
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5

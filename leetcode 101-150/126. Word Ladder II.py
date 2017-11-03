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


class Solution(object):
    def __init__(self):
        self.result = []
        self.word_list_set = set([])
        self.shortest_len = 99
        self.begin = ""
        self.end = ""

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        self.word_list_set = set(wordList)
        self.begin = beginWord
        self.end = endWord

        self.find_next_word(beginWord, set([]), [])
        results = []
        for result in self.result:
            if len(result) == self.shortest_len + 1:
                results.append(result)
        return results

    def find_next_word(self, curr_word, visited, path):
        if len(path) > self.shortest_len:
            return
        if curr_word == self.end:
            self.shortest_len = len(path)
            self.result.append([self.begin] + path)
        else:
            for i in xrange(len(curr_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    tmp_word = curr_word[:i] + c + curr_word[i + 1:]
                    if tmp_word not in visited and tmp_word in self.word_list_set:
                        new_visited = visited | set([tmp_word])
                        new_path = path + [tmp_word]
                        self.find_next_word(tmp_word, new_visited, new_path)


if __name__ == "__main__":
    assert Solution().findLadders("qa", "sq",
                                  ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le",
                                   "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn",
                                   "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc",
                                   "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co",
                                   "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an",
                                   "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io",
                                   "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]) == [
        ["a", "c"]
    ]
    assert Solution().findLadders("a", "c", ["a", "b", "c"]) == [
        ["a", "c"]
    ]
    assert Solution().findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]

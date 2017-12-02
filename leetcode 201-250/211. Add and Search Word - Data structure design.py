"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ..
A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.

You should be familiar with how a Trie works. If not, please work on this problem:
Implement Trie (Prefix Tree) first.

"""


class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.leaves:
                node.leaves[c] = TrieNode()
            node = node.leaves[c]
        node.is_string = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        else:
            return self.search_recu(self.root, word)

    def search_recu(self, node, word):
        if len(word) == 1:
            if word[0] == ".":
                for c in node.leaves:
                    if node.leaves[c].is_string:
                        return True
                return False
            if word[0] in node.leaves and node.leaves[word[0]].is_string:
                return True
            return False
        else:
            if word[0] in node.leaves:
                return self.search_recu(node.leaves[word[0]], word[1:])
            else:
                if word[0] == ".":
                    for c in node.leaves:
                        if self.search_recu(node.leaves[c], word[1:]):
                            return True
                    return False
                else:
                    return False


if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    assert obj.search("pad") is False
    assert obj.search("bad") is True
    assert obj.search("bad") is True
    assert obj.search("b..") is True

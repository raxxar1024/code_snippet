"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""


class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.leaves = {}


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for c in word:
            if c not in curr.leaves:
                curr.leaves[c] = TrieNode()
            curr = curr.leaves[c]
        curr.is_string = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.child_search(word)
        if node:
            return node.is_string
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.child_search(prefix) is not None

    def child_search(self, word):
        curr = self.root
        for c in word:
            if c in curr.leaves:
                curr = curr.leaves[c]
            else:
                return None
        return curr


if __name__ == "__main__":
    obj = Trie()
    obj.insert("abcdefg")
    assert obj.search("abcdefg") is True
    assert obj.startsWith("abc") is True

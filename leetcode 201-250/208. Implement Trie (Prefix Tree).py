"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """


if __name__ == "__main__":
    obj = Trie()
    obj.insert("abcdefg")
    assert obj.search("abcdefg") is True
    assert obj.startsWith("abc") is True

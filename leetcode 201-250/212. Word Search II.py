"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately.
What kind of data structure could answer such query efficiently? Does a hash table work?
Why or why not? How about a Trie?
If you would like to learn how to implement a basic trie,
please work on this problem: Implement Trie (Prefix Tree) first.

"""


class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.leaves = {}

    def insert(self, word):
        node = self
        for c in word:
            if c not in node.leaves:
                node.leaves[c] = TrieNode()
            node = node.leaves[c]
        node.is_string = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        visited = [[False for _ in xrange(len(board[0]))] for _ in xrange(len(board))]
        result = {}
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.findWords_recu(board, trie, i, j, visited, [], result)

        return result.keys()

    def findWords_recu(self, board, trie, i, j, visited, curr_word, result):
        if not trie or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return

        if board[i][j] not in trie.leaves:
            return

        visited[i][j] = True
        curr_word.append(board[i][j])

        next_node = trie.leaves[board[i][j]]
        if next_node.is_string:
            result["".join(curr_word)] = True

        self.findWords_recu(board, next_node, i - 1, j, visited, curr_word, result)
        self.findWords_recu(board, next_node, i + 1, j, visited, curr_word, result)
        self.findWords_recu(board, next_node, i, j - 1, visited, curr_word, result)
        self.findWords_recu(board, next_node, i, j + 1, visited, curr_word, result)

        visited[i][j] = False
        curr_word.pop()


if __name__ == "__main__":
    assert Solution().findWords([
        ["a", "b"], ["a", "a"]
    ], ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"]) == ['aba', 'aaa', 'aaab', 'baa', 'aaba']
    assert Solution().findWords([
        ["a", "b"], ["c", "d"]
    ], ["acdb"]) == ["acdb"]
    assert Solution().findWords([
        ["a", "b"]
    ], ["ba"]) == ["ba"]
    assert Solution().findWords([
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ], ["oath", "pea", "eat", "rain"]) == ["oath", "eat"]

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


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.leaves:
                node.leaves[c] = TrieNode()
            node = node.leaves[c]
        node.is_string = True

    def search(self, word):
        node = self.child_search(word)
        if node:
            return node.is_string
        else:
            return False

    def search_with(self, word):
        return self.child_search(word) is not None

    def child_search(self, word):
        node = self.root
        for c in word:
            if c in node.leaves:
                node = node.leaves[c]
            else:
                return None
        return node


class Solution(object):
    def __init__(self):
        self.result = []
        self.obj = Trie()

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        for word in words:
            self.obj.insert(word)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.check_start_with(i, j, board)
        return self.result

    def check_start_with(self, y, x, board):
        m = len(board[0])
        n = len(board)
        visited = [[False for _ in xrange(m)] for _ in xrange(n)]
        tmp_str = ""

        def check_start_with_recu(visited, tmp_str, y, x):
            tmp_str += board[y][x]
            visited[y][x] = True
            if self.obj.search_with(tmp_str):
                if self.obj.search(tmp_str):
                    if tmp_str not in self.result:
                        self.result.append(tmp_str)
                if x - 1 >= 0 and visited[y][x - 1] is False:
                    check_start_with_recu(visited, tmp_str, y, x - 1)
                    visited[y][x - 1] = False
                if x + 1 < m and visited[y][x + 1] is False:
                    check_start_with_recu(visited, tmp_str, y, x + 1)
                    visited[y][x + 1] = False
                if y - 1 >= 0 and visited[y - 1][x] is False:
                    check_start_with_recu(visited, tmp_str, y - 1, x)
                    visited[y - 1][x] = False
                if y + 1 < n and visited[y + 1][x] is False:
                    check_start_with_recu(visited, tmp_str, y + 1, x)
                    visited[y + 1][x] = False

        check_start_with_recu(visited, tmp_str, y, x)


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

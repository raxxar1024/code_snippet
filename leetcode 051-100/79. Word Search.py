"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visit = [[False for _ in xrange(len(board[0]))] for _ in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.check(board, word, i, j, 0, visit):
                    return True
        return False

    def check(self, board, word, i, j, idx, visit):
        if idx == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visit[i][j] or board[i][j] != word[idx]:
            return False

        visit[i][j] = True
        result = self.check(board, word, i + 1, j, idx + 1, visit) or \
                 self.check(board, word, i, j + 1, idx + 1, visit) or \
                 self.check(board, word, i - 1, j, idx + 1, visit) or \
                 self.check(board, word, i, j - 1, idx + 1, visit)
        visit[i][j] = False

        return result


if __name__ == "__main__":
    matrix = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    assert Solution().exist(matrix, "ABCCED") is True
    assert Solution().exist(matrix, "SEE") is True
    assert Solution().exist(matrix, "ABCB") is False

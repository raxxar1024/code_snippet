"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        from collections import deque
        queue = deque(())
        for i in xrange(len(board)):
            queue.append((0, i))
            queue.append((len(board[0]) - 1, i))

        for j in xrange(len(board[0])):
            queue.append((j, 0))
            queue.append((j, len(board) - 1))

        while queue:
            item = queue.popleft()
            i, j = item[0], item[1]
            if board[j][i] in ["O", "V"]:
                board[j][i] = "V"
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board[0]) and 0 <= y < len(board) and board[y][x] == "O":
                        queue.append((x, y))
                        board[y][x] = "V"

        for x in xrange(len(board[0])):
            for y in xrange(len(board)):
                if board[y][x] == "V":
                    board[y][x] = "O"
                else:
                    board[y][x] = "X"


if __name__ == "__main__":
    list_1 = [["X", "X", "X", "X"],
              ["X", "O", "O", "X"],
              ["X", "X", "O", "X"],
              ["X", "O", "X", "X"],
              ["X", "O", "X", "X"]]
    Solution().solve(list_1)
    assert list_1 == [["X", "X", "X", "X"],
                      ["X", "X", "X", "X"],
                      ["X", "X", "X", "X"],
                      ["X", "O", "X", "X"],
                      ["X", "O", "X", "X"]]

    list_1 = [["O", "O", "O"],
              ["O", "O", "O"],
              ["O", "O", "O"]]
    Solution().solve(list_1)
    assert list_1 == [["O", "O", "O"],
                      ["O", "O", "O"],
                      ["O", "O", "O"]]

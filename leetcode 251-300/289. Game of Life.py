"""
According to the Wikipedia's article:
"The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules
(taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite,
which would cause problems when the active area encroaches the border of the array.
How would you address these problems?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        """
        0:dead->dead
        1:live->live
        2:live->dead
        3:dead->live
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = 0
                for I in range(max(i - 1, 0), min(i + 2, m)):
                    for J in range(max(j - 1, 0), min(j + 2, n)):
                        if i == I and j == J:
                            continue
                        if board[I][J] in [1, 2]:
                            cnt += 1
                if board[i][j] == 1 and (cnt < 2 or 3 < cnt):
                    board[i][j] = 2
                elif board[i][j] == 0 and cnt == 3:
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                board[i][j] %= 2


if __name__ == "__main__":
    board = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
    Solution().gameOfLife(board)
    assert board == [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]

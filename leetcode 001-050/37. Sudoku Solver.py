class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def is_valid(x, y, board):
            for i in xrange(9):
                if board[i][y] == board[x][y] and i != x:
                    return False
            for i in xrange(9):
                if board[x][i] == board[x][y] and i != y:
                    return False
            for i in xrange(3):
                for j in xrange(3):
                    m, n = x/3*3+i, y/3*3+j
                    if board[m][n] == board[x][y] and m != x and n != y:
                        return False
            return True

        def solver(board):
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == '.':
                        for k in xrange(9):
                            board[i][j] = chr(ord("1") + k)
                            if is_valid(i, j, board) and solver(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        solver(board)


if __name__ == "__main__":
    board = [list("..9748..."), list("7........"), list(".2.1.9..."),
             list("..7...24."), list(".64.1.59."), list(".98...3.."),
             list("...8.3.2."), list("........6"), list("...2759..")]
    Solution().solveSudoku(board)
    assert board == [list("519748632"), list("783652419"), list("426139875"),
                     list("357986241"), list("264317598"), list("198524367"),
                     list("975863124"), list("832491756"), list("641275983")]

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_valid(x, y, t):
            for k in xrange(9):
                if board[k][y] == t and k != x:
                    return False
            for k in xrange(9):
                if board[x][k] == t and k != y:
                    return False
            for k in xrange(3):
                for l in xrange(3):
                    if board[x/3*3+k][y/3*3+l] == t and x != x/3*3+k and y != y/3*3+l:
                        return False
            return True

        for i in xrange(9):
            for j in xrange(9):
                tmp = board[i][j]
                if tmp == '.':
                    continue
                if is_valid(i, j, tmp) is False:
                    return False
        return True


if __name__ == "__main__":
    assert Solution().isValidSudoku(
        [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
         "9........"]
    ) is True



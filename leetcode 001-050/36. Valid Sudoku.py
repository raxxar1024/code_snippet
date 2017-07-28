class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_valid(xs):
            xs = filter(lambda x: x != '.', xs)
            return len(set(xs)) == len(xs)

        for i in xrange(9):
            if is_valid([board[i][j] for j in xrange(9)]) is False:
                return False
            if is_valid([board[j][i] for j in xrange(9)]) is False:
                return False

        for i in xrange(3):
            for j in xrange(3):
                if is_valid([board[i*3+m][j*3+n] for m in xrange(3) for n in xrange(3)]) is False:
                    return False

        return True


if __name__ == "__main__":
    assert Solution().isValidSudoku(
        [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
         "9........"]
    ) is True



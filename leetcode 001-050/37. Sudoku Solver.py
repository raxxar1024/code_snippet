class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """


if __name__ == "__main__":
    board = [list("..9748..."), list("7........"), list(".2.1.9..."),
             list("..7...24."), list(".64.1.59."), list(".98...3.."),
             list("...8.3.2."), list("........6"), list("...2759..")]
    Solution().solveSudoku(board)
    assert board == [list("519748632"), list("783652419"), list("426139875"),
                     list("357986241"), list("264317598"), list("198524367"),
                     list("975863124"), list("832491756"), list("641275983")]

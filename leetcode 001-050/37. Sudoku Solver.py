class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """


if __name__ == "__main__":
    board = ["..9748...", "7........", ".2.1.9...",
             "..7...24.", ".64.1.59.", ".98...3..",
             "...8.3.2.", "........6", "...2759.."]
    Solution().solveSudoku(board)
    assert board == ["519748632", "783652419", "426139875",
                     "357986241", "264317598", "198524367",
                     "975863124", "832491756", "641275983"]

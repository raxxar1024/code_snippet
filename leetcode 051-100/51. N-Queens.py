"""
The n-queens puzzle is the problem of placing n queens on an n*n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        positions = []

        def DFS(ys, xy_diff, xy_sum):
            if n == len(ys):
                positions.append(ys)
                return
            else:
                x = len(ys)
                for y in xrange(n):
                    if y not in ys and (x - y) not in xy_diff and (x + y) not in xy_sum:
                        DFS(ys + [y], xy_diff + [x - y], xy_sum + [x + y])

        DFS([], [], [])

        results = []
        for i in xrange(len(positions)):
            results.append(["." * k + "Q" + "." * (n - k - 1) for k in positions[i]])

        return results


if __name__ == "__main__":
    assert Solution().solveNQueens(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    # print Solution().solveNQueens(7)

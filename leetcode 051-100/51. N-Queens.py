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

        def DFS(xs, ys, xy_diff, xy_sum):
            if n == len(xs):
                positions.append([xs, ys])
                return
            for x in xrange(n):
                for y in xrange(n):
                    if x not in xs and y not in ys and (x - y) not in xy_diff and (x + y) not in xy_sum:
                        DFS(xs + [x], ys + [y], xy_diff + [x - y], xy_sum + [x + y])

        DFS([], [], [], [])

        def convert_pos_matrix(position):
            tmp = [["." for i in xrange(n)] for j in xrange(n)]
            result = []
            xs, ys = position[0], position[1]
            for i in xrange(len(xs)):
                tmp[xs[i]][ys[i]] = "Q"
            for i in xrange(len(tmp)):
                result.append("".join(tmp[i]))

            return result

        results = []
        for k in xrange(len(positions)):
            tmp_result = convert_pos_matrix(positions[k])
            if tmp_result not in results:
                results.append(tmp_result)

        return results


if __name__ == "__main__":
    assert Solution().solveNQueens(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]

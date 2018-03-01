"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
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

        return len(positions)


if __name__ == "__main__":
    assert Solution().totalNQueens(1) == 1

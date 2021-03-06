"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city
when viewed from a distance.
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A),
write a program to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi],
where Li and Ri are the x coordinates of the left and right edge of the ith building,
respectively, and Hi is its height.
It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as:
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of
[ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline.
A key point is the left endpoint of a horizontal line segment.
Note that the last key point, where the rightmost building ends,
is merely used to mark the termination of the skyline, and always has zero height.
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:
[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable;
the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
Credits:
Special thanks to @stellari for adding this problem, creating these two awesome images and all test cases.

"""


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        heights = sorted([(b[0], -b[2]) for b in buildings] + [(b[1], b[2]) for b in buildings],
                         cmp=lambda x, y: cmp(x[0], y[0]) if x[0] != y[0] else cmp(x[1], y[1]))

        height_stack, max_height, result = [0], 0, []
        for h in heights:
            if h[1] < 0:
                if -h[1] > max_height:
                    max_height = -h[1]
                    result.append([h[0], -h[1]])
                height_stack.append(-h[1])
            else:
                height_stack.remove(h[1])
                if h[1] == max_height:
                    max_height = max(height_stack)
                if h[1] > max_height:
                    result.append([h[0], max_height])

        return result


if __name__ == "__main__":
    assert Solution().getSkyline([[0, 2147483647, 2147483647]]) == [[0, 2147483647], [2147483647, 0]]
    assert Solution().getSkyline([]) == []
    assert Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]) == [
        [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]
    ]

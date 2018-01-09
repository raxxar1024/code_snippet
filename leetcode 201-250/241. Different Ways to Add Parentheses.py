"""
Given a string of numbers and operators,
return all possible results from computing all the different possible ways to group numbers and operators.
The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        import re
        import operator
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({"+": operator.add, "-": operator.sub, "*": operator.mul}.get, tokens[1::2])
        lookups = [[None for _ in xrange(len(nums))] for _ in xrange(len(nums))]

        def diffWaysToComputeRecu(left, right):
            if left == right:
                return [nums[left]]
            if lookups[left][right]:
                return lookups[left][right]
            lookups[left][right] = [ops[i](x, y)
                                    for i in xrange(left, right)
                                    for x in diffWaysToComputeRecu(left, i)
                                    for y in diffWaysToComputeRecu(i + 1, right)
                                    ]
            return lookups[left][right]

        return sorted(diffWaysToComputeRecu(0, len(nums) - 1))


if __name__ == "__main__":
    assert Solution().diffWaysToCompute("2-1-1") == [0, 2]
    assert Solution().diffWaysToCompute("2*3-4*5") == [-34, -14, -10, -10, 10]

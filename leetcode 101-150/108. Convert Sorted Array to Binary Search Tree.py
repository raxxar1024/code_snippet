"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """


if __name__ == "__main__":
    tree_1 = Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
    assert tree_1.val == 1
    assert tree_1.left.val == 2
    assert tree_1.right.val == 3
    assert tree_1.left.left.val == 4
    assert tree_1.left.right.val == 5
    assert tree_1.right.left.val == 6
    assert tree_1.right.right.val == 7

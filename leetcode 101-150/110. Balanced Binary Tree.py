"""
Given a binary tree, determine if it is height-balanced.

For this problem,
a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


if __name__ == "__main__":
    tree_1 = TreeNode(3)
    tree_1.left = TreeNode(9)
    tree_1.right = TreeNode(20)
    tree_1.right.left = TreeNode(15)
    tree_1.right.right = TreeNode(7)
    assert Solution().isBalanced(tree_1) is True
    tree_1.right.left.left = TreeNode(1)
    assert Solution().isBalanced(tree_1) is False

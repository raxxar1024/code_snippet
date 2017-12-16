"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


if __name__ == "__main__":
    node_1 = TreeNode(1)
    node_1.left = TreeNode(2)
    node_1.right = TreeNode(3)
    node_1.left.left = TreeNode(4)
    node_1.left.right = TreeNode(5)
    node_1.right.left = TreeNode(6)
    assert Solution().countNodes(node_1) == 6

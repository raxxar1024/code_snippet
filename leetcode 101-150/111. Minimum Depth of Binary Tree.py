"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == "__main__":
    tree_1 = TreeNode(3)
    tree_1.left = TreeNode(9)
    tree_1.right = TreeNode(20)
    tree_1.right.left = TreeNode(15)
    tree_1.right.right = TreeNode(7)
    assert Solution().minDepth(tree_1) == 2

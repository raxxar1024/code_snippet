"""
Given a binary tree, find the maximum path sum.

For this problem,
a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    max_path = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathSumRecu(root)
        return self.max_path

    def maxPathSumRecu(self, root):
        if root is None:
            return 0
        max_left = max(0, self.maxPathSumRecu(root.left))
        max_right = max(0, self.maxPathSumRecu(root.right))
        self.max_path = max(self.max_path, max_left + max_right + root.val)
        return max(max_left, max_right) + root.val


if __name__ == "__main__":
    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(3)
    assert Solution().maxPathSum(tree_1) == 6

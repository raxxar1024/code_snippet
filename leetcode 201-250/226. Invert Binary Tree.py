"""
Invert a binary tree.
     4
   |   |
  2     7
 | |   | |
1   3 6   9
to
     4
   |   |
  7     2
 | |   | |
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew),
but you can't invert a binary tree on a whiteboard so fuck off.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == "__main__":
    node = TreeNode(4)
    node.left = TreeNode(2)
    node.right = TreeNode(7)
    node.left.left = TreeNode(1)
    node.left.right = TreeNode(3)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(9)
    invert_tree = Solution().invertTree(node)
    assert invert_tree.val == 4
    assert invert_tree.left.val == 7
    assert invert_tree.right.val == 2
    assert invert_tree.left.left.val == 9
    assert invert_tree.left.right.val == 6
    assert invert_tree.right.left.val == 3
    assert invert_tree.right.right.val == 1

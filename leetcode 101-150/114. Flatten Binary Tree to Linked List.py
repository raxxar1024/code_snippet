"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree,
each node's right child points to the next node of a pre-order traversal.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """


if __name__ == "__main__":
    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.left.left = TreeNode(3)
    tree_1.left.right = TreeNode(4)
    tree_1.right = TreeNode(5)
    tree_1.right.right = TreeNode(6)
    Solution().flatten(tree_1)
    assert tree_1.val == 1
    assert tree_1.right.val == 2
    assert tree_1.right.right.val == 3
    assert tree_1.right.right.right.val == 4
    assert tree_1.right.right.right.right.val == 5
    assert tree_1.right.right.right.right.right.val == 6

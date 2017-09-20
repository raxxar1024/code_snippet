"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST_2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid_BST_recu(root, float("-inf"), float("inf"))

    def is_valid_BST_recu(self, node, low, high):
        if not node:
            return True
        return low < node.val < high and self.is_valid_BST_recu(node.left, low, node.val) and self.is_valid_BST_recu(
            node.right, node.val, high)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev, curr = None, root
        while curr:
            if not curr.left:
                if prev and prev.val >= curr.val:
                    return False
                prev = curr
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right
                if not node.right:
                    node.right = curr
                    curr = curr.left
                else:
                    if prev and prev.val >= curr.val:
                        return False
                    node.right = None
                    prev = curr
                    curr = curr.right
        return True


if __name__ == "__main__":
    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(1)
    tree_1.right = TreeNode(3)
    assert Solution().isValidBST(tree_1) is True

    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(3)
    assert Solution().isValidBST(tree_1) is False

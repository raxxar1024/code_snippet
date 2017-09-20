"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q:
            return False
        if p and q is None:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(3)
    assert Solution().isSameTree(tree_1, None) is False
    assert Solution().isSameTree(tree_1, tree_1) is True

    tree_2 = TreeNode(2)
    tree_2.left = TreeNode(1)
    tree_2.right = TreeNode(3)
    assert Solution().isSameTree(tree_1, tree_2) is False

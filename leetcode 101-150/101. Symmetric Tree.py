"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric_2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True
        else:
            def is_mirror(p, q):
                if p is None and q is None:
                    return True
                if p and q:
                    return p.val == q.val and is_mirror(p.left, q.right) and is_mirror(p.right, q.left)
                return False

            return is_mirror(root.left, root.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            p, q = stack.pop(), stack.pop()
            if p is None and q is None:
                continue
            if p is None or q is None or p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)

            stack.append(q.left)
            stack.append(p.right)

        return True


if __name__ == "__main__":
    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(2)
    assert Solution().isSymmetric(tree_1) is True

    tree_1.right = TreeNode(3)
    assert Solution().isSymmetric(tree_1) is False

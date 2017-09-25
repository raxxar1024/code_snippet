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
        if root is None:
            return True

        def get_depth(r):
            depth = 0
            if r is None:
                return depth
            current = [r]
            while current:
                depth += 1
                next_level = []
                for node in current:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                current = next_level
            return depth

        depth_1 = get_depth(root.left)
        depth_2 = get_depth(root.right)
        if abs(depth_1 - depth_2) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False


if __name__ == "__main__":
    tree_1 = TreeNode(3)
    tree_1.left = TreeNode(9)
    tree_1.right = TreeNode(20)
    tree_1.right.left = TreeNode(15)
    tree_1.right.right = TreeNode(7)
    assert Solution().isBalanced(tree_1) is True
    tree_1.right.left.left = TreeNode(1)
    assert Solution().isBalanced(tree_1) is False

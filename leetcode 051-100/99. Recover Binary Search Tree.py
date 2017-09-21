"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prev, curr = None, root
        invalid_pair = [None, None]

        def detect_broken(pair, p, c):
            if p and p.val >= c.val:
                if pair[0] is None:
                    pair[0] = p
                pair[1] = c

        while curr:
            if curr.left is None:
                detect_broken(invalid_pair, prev, curr)
                prev = curr
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right
                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    detect_broken(invalid_pair, prev, curr)
                    node.right = None
                    prev = curr
                    curr = curr.right
        invalid_pair[0].val, invalid_pair[1].val = invalid_pair[1].val, invalid_pair[0].val


if __name__ == "__main__":
    tree_1 = TreeNode(2)
    tree_1.left = TreeNode(3)
    tree_1.right = TreeNode(1)
    Solution().recoverTree(tree_1)
    assert tree_1.val == 2
    assert tree_1.left.val == 1
    assert tree_1.right.val == 3

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumbersRecu(root, 0)

    def sumNumbersRecu(self, node, tmp_num):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return tmp_num * 10 + node.val
        return self.sumNumbersRecu(node.left, tmp_num * 10 + node.val) + self.sumNumbersRecu(node.right,
                                                                                             tmp_num * 10 + node.val)


if __name__ == "__main__":
    tree_1 = TreeNode(1)
    tree_1.left = TreeNode(2)
    tree_1.right = TreeNode(3)
    assert Solution().sumNumbers(tree_1) == 25

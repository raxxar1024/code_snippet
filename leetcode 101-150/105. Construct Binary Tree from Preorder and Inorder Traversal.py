"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        if len(preorder) == 1:
            return root

        idx = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root


if __name__ == "__main__":
    tree_1 = Solution().buildTree([1, 2, 4, 5, 3, 6, 8, 7], [4, 2, 5, 1, 6, 8, 3, 7])
    assert tree_1.val == 1
    assert tree_1.left.val == 2
    assert tree_1.right.val == 3
    assert tree_1.left.left.val == 4
    assert tree_1.left.right.val == 5
    assert tree_1.right.left.val == 6
    assert tree_1.right.right.val == 7
    assert tree_1.right.left.right.val == 8

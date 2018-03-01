"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
"The lowest common ancestor is defined between two nodes v and w as the lowest node in T
that has both v and w as descendants (where we allow a node to be a descendant of itself)."

        _______6_______
       |               |
    ___2___          __8__
   |       |        |     |
   0      _4_       7     9
         |   |
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        s, e = sorted([p.val, q.val])
        while not s <= root.val <= e:
            root = root.left if s <= root.val else root.right
        return root


if __name__ == "__main__":
    node_6 = TreeNode(6)
    node_6.left = node_2 = TreeNode(2)
    node_6.right = node_8 = TreeNode(8)
    node_2.left = node_0 = TreeNode(0)
    node_2.right = node_4 = TreeNode(4)
    node_4.left = node_3 = TreeNode(3)
    node_4.right = node_5 = TreeNode(5)
    node_8.left = node_7 = TreeNode(7)
    node_8.right = node_9 = TreeNode(9)
    assert Solution().lowestCommonAncestor(node_6, node_2, node_8) == node_6
    assert Solution().lowestCommonAncestor(node_6, node_2, node_4) == node_2

    node_5.left = node_3
    node_5.right = node_6
    node_3.left = node_1 = TreeNode(1)
    node_3.right = node_4
    node_1.left = None
    node_1.right = node_2
    node_2.left = node_2.right = node_4.left = node_4.right = node_6.left = node_6.right = None
    assert Solution().lowestCommonAncestor(node_5, node_2, node_4) == node_3

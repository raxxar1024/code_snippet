"""
Given a binary tree and a sum,
find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """


if __name__ == "__main__":
    tree_1 = TreeNode(5)
    tree_1.left = TreeNode(4)
    tree_1.left.left = TreeNode(11)
    tree_1.left.left.left = TreeNode(7)
    tree_1.left.left.right = TreeNode(2)
    tree_1.right = TreeNode(8)
    tree_1.right.left = TreeNode(13)
    tree_1.right.right = TreeNode(4)
    tree_1.right.right.left = TreeNode(5)
    tree_1.right.right.right = TreeNode(1)
    assert Solution().pathSum(tree_1, 22) == [
        [5, 4, 11, 2],
        [5, 8, 4, 5]
    ]

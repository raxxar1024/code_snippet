"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result, current, dir = [], [root], True
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if dir:
                result.append(vals)
            else:
                result.append(vals[::-1])
            dir = not dir
            current = next_level
        return result


if __name__ == "__main__":
    tree_1 = TreeNode(3)
    tree_1.left = TreeNode(9)
    tree_1.right = TreeNode(20)
    tree_1.right.left = TreeNode(15)
    tree_1.right.right = TreeNode(7)
    assert Solution().zigzagLevelOrder(tree_1) == [
        [3],
        [20, 9],
        [15, 7]
    ]

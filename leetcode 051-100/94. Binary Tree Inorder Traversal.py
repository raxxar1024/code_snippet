"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        

if __name__ == "__main__":
    t1, t2, t3 = TreeNode(1), TreeNode(2), TreeNode(3)
    t1.right = t2
    t2.left = t3
    assert Solution().inorderTraversal(t1) == [1, 3, 2]

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
        result = []
        curr = root
        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if not node.right:
                    node.right = curr
                    curr = curr.left
                else:
                    result.append(curr.val)
                    # node.right = None # this line can be added if want to hold whole tree no change
                    curr = curr.right
        return result

    def inorderTraversal_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def get_node_result(node):
            if not node:
                return
            get_node_result(node.left)
            result.append(node.val)
            get_node_result(node.right)
            return

        get_node_result(root)
        return result


if __name__ == "__main__":
    t1, t2, t3 = TreeNode(1), TreeNode(2), TreeNode(3)
    t1.right = t2
    t2.left = t3
    assert Solution().inorderTraversal(t1) == [1, 3, 2]

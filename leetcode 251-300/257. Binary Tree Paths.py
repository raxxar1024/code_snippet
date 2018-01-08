"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def binaryTreePath_recu(node, path):
            if not node:
                return
            if node.left or node.right:
                binaryTreePath_recu(node.left, path + [str(node.val)])
                binaryTreePath_recu(node.right, path + [str(node.val)])
            else:
                result.append("->".join(path + [str(node.val)]))

        if not root:
            return []
        result = []
        binaryTreePath_recu(root, [])
        return result


if __name__ == "__main__":
    node_1 = TreeNode(1)
    assert Solution().binaryTreePaths(node_1) == ["1"]
    node_1.left = TreeNode(2)
    node_1.right = TreeNode(3)
    node_1.left.right = TreeNode(5)
    assert Solution().binaryTreePaths(node_1) == ["1->2->5", "1->3"]

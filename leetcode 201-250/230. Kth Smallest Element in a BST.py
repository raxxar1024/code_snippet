"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s, curr, rank = [], root, 0

        while s or curr:
            if curr:
                s.append(curr)
                curr = curr.left
            else:
                curr = s.pop()
                rank += 1
                if rank == k:
                    return curr.val
                curr = curr.right

        return float("-inf")


if __name__ == "__main__":
    node_1 = TreeNode(4)
    node_1.left = TreeNode(2)
    node_1.left.left = TreeNode(1)
    node_1.left.right = TreeNode(3)
    node_1.right = TreeNode(6)
    node_1.right.left = TreeNode(5)
    node_1.right.right = TreeNode(7)
    assert Solution().kthSmallest(node_1, 1) == 1
    assert Solution().kthSmallest(node_1, 2) == 2
    assert Solution().kthSmallest(node_1, 3) == 3
    assert Solution().kthSmallest(node_1, 4) == 4
    assert Solution().kthSmallest(node_1, 5) == 5
    assert Solution().kthSmallest(node_1, 6) == 6
    assert Solution().kthSmallest(node_1, 7) == 7

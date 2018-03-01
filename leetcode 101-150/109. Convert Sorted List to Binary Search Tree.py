"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def sorted_array_to_BST(nums):
            if len(nums) == 0:
                return None
            mid = len(nums) / 2
            root = TreeNode(nums[mid])
            root.left = sorted_array_to_BST(nums[:mid])
            root.right = sorted_array_to_BST(nums[mid + 1:])
            return root

        return sorted_array_to_BST(nums)


if __name__ == "__main__":
    list_1 = ListNode(1)
    list_1.next = ListNode(2)
    list_1.next.next = ListNode(3)
    list_1.next.next.next = ListNode(4)
    list_1.next.next.next.next = ListNode(5)
    list_1.next.next.next.next.next = ListNode(6)
    list_1.next.next.next.next.next.next = ListNode(7)

    tree_1 = Solution().sortedListToBST(list_1)
    assert tree_1.val == 4
    assert tree_1.left.val == 2
    assert tree_1.right.val == 6
    assert tree_1.left.left.val == 1
    assert tree_1.left.right.val == 3
    assert tree_1.right.left.val == 5
    assert tree_1.right.right.val == 7

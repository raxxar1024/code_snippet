"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_1.next = ListNode(2)
    node_1.next.next = ListNode(3)
    res_node = Solution().reverseList(node_1)
    assert res_node.val == 3
    assert res_node.next.val == 2
    assert res_node.next.next.val == 1

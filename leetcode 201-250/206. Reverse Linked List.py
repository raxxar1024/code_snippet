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
    def reverseList_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

    def reverseList(self, head):
        return self.reverse_recur(head, None)

    def reverse_recur(self, head, new_head):
        if head is None:
            return new_head
        next = head.next
        head.next = new_head
        return self.reverse_recur(next, head)


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_1.next = ListNode(2)
    node_1.next.next = ListNode(3)
    res_node = Solution().reverseList(node_1)
    assert res_node.val == 3
    assert res_node.next.val == 2
    assert res_node.next.next.val == 1

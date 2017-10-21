"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1.next = node_2
    node_1.next.next = node_3
    node_1.next.next.next = node_4
    node_1.next.next.next.next = node_5
    assert Solution().hasCycle(node_1) is False
    node_5.next = node_1
    assert Solution().hasCycle(node_1) is True

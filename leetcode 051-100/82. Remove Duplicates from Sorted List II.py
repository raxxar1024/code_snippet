"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


if __name__ == "__main__":
    l1, l1.next, l1.next.next, l1.next.next.next, l1.next.next.next.next, l1.next.next.next.next.next, l1.next.next.next.next.next.next = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(3), ListNode(4), ListNode(4), ListNode(5)
    result = Solution().deleteDuplicates(l1)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 5

    l1, l1.next, l1.next.next, l1.next.next.next, l1.next.next.next.next = \
        ListNode(1), ListNode(1), ListNode(1), ListNode(2), ListNode(3)
    result = Solution().deleteDuplicates(l1)
    assert result.val == 2
    assert result.next.val == 3

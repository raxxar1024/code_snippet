"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast, slow, prev = fast.next.next, slow.next, slow
        prev.next = None

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, list_1, list_2):
        dummy = curr = ListNode(0)

        while list_1 and list_2:
            if list_1.val < list_2.val:
                curr.next = list_1
                list_1 = list_1.next
            else:
                curr.next = list_2
                list_2 = list_2.next
            curr = curr.next

        if list_1:
            curr.next = list_1
        if list_2:
            curr.next = list_2
        return dummy.next


if __name__ == "__main__":
    node_2 = ListNode(2)
    node_2.next = ListNode(1)
    node_2.next.next = ListNode(4)
    node_2.next.next.next = ListNode(3)
    node_r = Solution().sortList(node_2)
    assert node_r.val == 1
    assert node_r.next.val == 2
    assert node_r.next.next.val == 3
    assert node_r.next.next.next.val == 4

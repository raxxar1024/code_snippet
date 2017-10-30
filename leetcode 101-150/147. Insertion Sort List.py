"""
Sort a linked list using insertion sort.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = curr = head
        while curr.next:
            if curr.next.val < curr.val:
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next
                tmp = curr.next
                curr.next = curr.next.next
                tmp.next = prev.next
                prev.next = tmp
            else:
                curr = curr.next
        return dummy.next


if __name__ == "__main__":
    node_2 = ListNode(2)
    node_2.next = ListNode(1)
    node_2.next.next = ListNode(4)
    node_2.next.next.next = ListNode(3)
    node_r = Solution().insertionSortList(node_2)
    assert node_r.val == 1
    assert node_r.next.val == 2
    assert node_r.next.next.val == 3
    assert node_r.next.next.next.val == 4

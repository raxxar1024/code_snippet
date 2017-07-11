# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p1, p2 = dummy, dummy
        dummy.next = head
        for i in xrange(n):
            p1 = p1.next

        tmp = p2
        while p1.next:
            p2 = p2.next
            p1 = p1.next
        p2.next = p2.next.next

        return tmp.next


if __name__ == "__main__":
    l1, l1.next = ListNode(1), ListNode(2)
    result = Solution().removeNthFromEnd(l1, 1)
    assert result.val == 1

    l1, l1.next, l1.next.next, l1.next.next.next, l1.next.next.next.next = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    result = Solution().removeNthFromEnd(l1, 2)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 5


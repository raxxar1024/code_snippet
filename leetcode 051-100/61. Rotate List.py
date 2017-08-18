"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        prev = ListNode(-1)
        prev.next = head
        tmp = head
        count = 0
        while tmp:
            if tmp.next is None:
                tmp.next = head
                break
            tmp = tmp.next
            count += 1

        k %= (count+1)
        for i in xrange(count + 1 - k):
            tmp = tmp.next

        prev.next = tmp.next
        tmp.next = None

        return prev.next


if __name__ == "__main__":
    result = Solution().rotateRight([], 2)
    assert result.val == 4
    assert result.next.val == 5
    assert result.next.next.val == 1
    assert result.next.next.next.val == 2
    assert result.next.next.next.next.val == 3

    l1, l1.next, l1.next.next, l1.next.next.next, l1.next.next.next.next = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    result = Solution().rotateRight(l1, 2)
    assert result.val == 4
    assert result.next.val == 5
    assert result.next.next.val == 1
    assert result.next.next.next.val == 2
    assert result.next.next.next.next.val == 3

    l1, l1.next, l1.next.next, l1.next.next.next, l1.next.next.next.next = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    result = Solution().rotateRight(l1, 1)
    assert result.val == 5
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 4

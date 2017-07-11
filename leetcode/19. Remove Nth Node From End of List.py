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

        length = 0
        idx = 0
        result_tmp = ListNode(0)
        result = result_tmp

        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next

        tmp = head
        while tmp:
            if idx != length-n:
                result_tmp.next = ListNode(tmp.val)
                result_tmp = result_tmp.next
            tmp = tmp.next
            idx += 1

        return result.next


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


"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy, curr, diff = ListNode(-1), head, n - m + 1
        dummy.next = curr

        last_un_swap = dummy
        while curr and m > 1:
            curr, last_un_swap, m = curr.next, curr, m - 1

        prev, first_swap = last_un_swap, curr
        while curr and diff > 0:
            curr.next, prev, curr, diff = prev, curr, curr.next, diff - 1

        last_un_swap.next, first_swap.next = prev, curr

        return dummy.next


if __name__ == "__main__":
    l1, l1.next, l1.next.next, l1.next.next.next, l1.next.next.next.next = \
        ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    result = Solution().reverseBetween(l1, 2, 4)
    assert result.val == 1
    assert result.next.val == 4
    assert result.next.next.val == 3
    assert result.next.next.next.val == 2
    assert result.next.next.next.next.val == 5

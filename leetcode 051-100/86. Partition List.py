"""
Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """


if __name__ == "__main__":
    l1, l1.next, l1.next.next, l1.next.next.next, l1.next.next.next.next, l1.next.next.next.next.next = \
        ListNode(1), ListNode(4), ListNode(3), ListNode(2), ListNode(5), ListNode(2)
    result = Solution().partition(l1, 3)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 2
    assert result.next.next.next.val == 4
    assert result.next.next.next.next.val == 3
    assert result.next.next.next.next.next.val == 5
